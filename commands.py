import telegram
from telegram.ext import (CommandHandler, ConversationHandler, RegexHandler)
from database import houseDB, chatDB, stationDB
from stationInfo import stations, keyStations, key_station_passwords

# ===== Enable logging ======
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)


# ===== Global variables =====
HOUSES = ("Ursaia", "Nocturna", "Ianthe", "Triton", "Ankaa", "Saren")
CONFIRMATION_REQUEST = 1
NUM_OPTIONAL_STATIONS = 10 # Change!
NUM_KEY_STATIONS = 4


# ====== Bot commands ======

# /start
# After user enters "/start", the bot will prompt the user for their house (Ursaia, Nocturna, Ianthe, Ankaa, Saren) using custom keyboard
# After user enters their house, the bot will automatically call the registerHouse() method, 
# evaluating whether that house is already registered in our database and output the corresponding messages
def start(bot, update):
    user = update.message.from_user.username
    reply_keyboard = [['Ursaia'], ['Nocturna'], ['Ianthe'], ['Triton'], ['Ankaa'], ['Saren']]
    reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    text = "@" + user + " Please Choose Your House! (Type '/cancel' to quit)"
    update.message.reply_text(text= text, reply_markup = reply_markup)
    return CONFIRMATION_REQUEST


# This method should be automatically called after the user enters their house.
# Evaluates whether that house is already registered in our database or not
def registerHouse(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    if (chatDB.is_house_registered(text)):
        update.message.reply_text(text = "What! This house has already been registered. Wanna check again? Type '/start' to choose another house", reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END
    elif (chatDB.is_chat_registered(chat_id)):
        update.message.reply_text(text = "This chat has already been assigned a house! Type '/remove' to remove this chat's house, then '/start' to register a house.", reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        # reply_keyboard = [["/my_house_letters", "/all_house_letters"]]
        # reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard)
        chatDB.add_house(chat_id, text)
        house = chatDB.get_house(chat_id)
        logger.info("Team %s has been registered by %s.", text, update.message.from_user.first_name)
        update.message.reply_text(text = "AWESOME! {} will be my favourite house now!".format(text))
        # bot.sendMessage(chat_id=chat_id,text = "Press '/my_house_letters' to see the letter(s) {} has collected.\n\nPress '/all_house_letters' to see the letter(s) that other houses have collected.".format(house), replymark_up=reply_markup)
        bot.sendMessage(chat_id=chat_id,text = "Press '/help' to see a list of commands and instructions.")


# /remove
# Ends the conversation that was initiated by '/start'. Allows a chat to remove its house.
def remove(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        house = chatDB.get_house(chat_id)
        chatDB.remove_chat(chat_id)
        message = "House removed! Please re-register your house immediately by typing '/start' before you continue."
        logger.info("%s has been removed from the chatDB by %s.", house, update.message.from_user.first_name)
    else:
        message = "Chat not registered yet."

    bot.send_message(chat_id=chat_id, text=message)
    return ConversationHandler.END


# /play
def play(bot, update):
    chat_id = update.message.chat_id
    message = "Station number?"
    bot.send_message(chat_id=chat_id, text=message)
    return CONFIRMATION_REQUEST


# Callback function for station instructions
def get_instructions(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    if ((text).isdigit()):
        stationNumber = int(text)
        station = stations.get(stationNumber)
        if station == None:
            logger.info("%s calling non-existent station %s.", update.message.from_user.first_name, stationNumber)
            message = "Station number " + str(stationNumber) + " doesn't exist."
        else:
            message = station.print_instructions()
    else:
        message = "Station " + text + " doesn't exist."

    logger.info("%s requesting instructions for station %s.", update.message.from_user.first_name, text)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")
    return ConversationHandler.END

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


# dummy callback for conversation ender
def cancel(bot, update):
    return ConversationHandler.END


# /help
def help(bot, update):
    chat_id = update.message.chat_id
    message = """Upon reaching station:
    /play - To receive instructions for the mission. I'll prompt you for the station number
    After completing the mission, OGLs will give you a password to unlock the station's letters.
    
    Other commands:
    /my_house_letters - View your house letters
    /all_house_letters - View all house letters
    /station_overview - Overview of all station locations and letters available. Note which letters are running out!!
    /start - Register your house
    /remove - Unregister your house"""

    logger.info("%s requesting help.", update.message.from_user.first_name)
    bot.send_message(chat_id=chat_id, text=message)


# /my_house_letters
def my_house_letters(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        house = chatDB.get_house(chat_id)
        letters = houseDB.get_house_letters(house) 
        message = "*" + house + "*:\n" + "\n".join(letters)

        logger.info("%s from %s wants to view their letters.", update.message.from_user.first_name, house)
    else:
        message = "Chat not registered yet."
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")


# /all_house_letters
def all_house_letters(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        message = ""
        for house in HOUSES:
            letters = houseDB.get_house_letters(house)
            message = message + "*" + house + "*:\n" + ", ".join(letters) + "\n"

        house = chatDB.get_house(chat_id)
        logger.info("%s from %s wants to view all house letters.", update.message.from_user.first_name, house)
    else:
        message = "Chat not registered yet."

    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")


# /station_overview
def station_overview(bot, update):
    chat_id = update.message.chat_id
    message = ""
    for stnNum in keyStations:
        keyStn = keyStations[stnNum]
        message = message + keyStn.print_station() + "\n"
    for stnNum in range(1, NUM_OPTIONAL_STATIONS + 1):
        letters_left = str(stationDB.get_letters_left(stnNum))
        message = message + stations[stnNum].print_station() + "Redemptions left - " + letters_left + "\n\n"

    logger.info("%s wants to view station overview.", update.message.from_user.first_name)
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")

# ========= end ==========

# Callback for station completion (when a password is keyed in to obtain a letter)
def station_complete(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        text = update.message.text
        house = chatDB.get_house(chat_id)
        found_match = False
        for stnNum in range(1, NUM_OPTIONAL_STATIONS + 1):
            stn = stations[stnNum]
            # If password is correct, and there are letters left, and the house has not already collected them
            if (text == stn.password and stationDB.get_letters_left(stnNum) > 0 and not houseDB.already_collected(house, stn.letters[0])):
                found_match = True
                give_house_letters(bot, chat_id, stn.letters)
                
                # Decrease letter count
                stationDB.decrease_letter_count(stnNum)
                break
        if (not found_match):
            match = key_station_passwords.get(text)
            if (match != None and not houseDB.already_collected(house, match[0])):
                give_house_letters(bot, chat_id, match)


def give_house_letters(bot, chat_id, letters):
    # Add letters to house
    house = chatDB.get_house(chat_id)
    houseDB.add_letters(house, letters)

    logger.info("%s added to %s.", ', '.join(letters), house)
    message = "Unlocked: " + ', '.join(letters) + "!"
    bot.send_message(chat_id=chat_id, text=message)


# =======================

# Registers command in the dispatcher
def registerCommand(dispatcher, commandStr, callback):
        handler = CommandHandler(commandStr, callback)
        dispatcher.add_handler(handler)

