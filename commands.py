import telegram
from telegram.ext import (CommandHandler, ConversationHandler, RegexHandler)
from database import houseDB, chatDB

# ===== Enable logging ======
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== Global variables =====
HOUSES = ("Ursaia", "Nocturna", "Ianthe", "Triton", "Ankaa", "Saren")
CONFIRMATION_REQUEST = 1



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
# It it is, the bot will output "What! Wanna check again?! (Type '/start' to choose another house)" 
# Else, the bot will add the chat id and the house into our database and output " AWESOME! <name of house> will be my favourite house now!" 
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
        reply_keyboard = [["/my_house_letters", "/all_house_letters"]]
        reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard)
        chatDB.add_house(chat_id, text)
        house = chatDB.get_house(chat_id)
        logger.info("Team %s has been registered by %s.", text, update.message.from_user.first_name)
        update.message.reply_text(text = "AWESOME! Team {} will be my favourite house now!".format(text), reply_markup=reply_markup)
        bot.sendMessage(chat_id=chat_id,text = "Press '/my_house_letters' to see the letter(s) Team {} has collected.\n\nPress '/all_house_letters' to see the letter(s) that other houses have collected.".format(house), replymark_up=reply_markup)


# /remove
# Ends the conversation that was initiated by '/start'. Allows a chat to remove its house.
def remove(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        house = chatDB.get_house(chat_id)
        chatDB.remove_chat(chat_id)
        message = "House removed! Please re-register your house immediately before you continue."
        logger.info("%s has been removed from the chatDB by %s.", house, update.message.from_user.first_name)
    else:
        message = "Chat not registered yet."
    
    bot.send_message(chat_id=chat_id, text=message)
    return ConversationHandler.END


# /my_house_letters
def my_house_letters(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        house = chatDB.get_house(chat_id)
        letters = houseDB.get_house_letters(house) 
        message = house + ":\n" + "\n".join(letters)

        # Logger
        logger.info("%s from Team %s wants to view their letters.", update.message.from_user.first_name, house)
    else:
        message = "Chat not registered yet."
    # reply_keyboard = [["/my_house_letters", "/all_house_letters"]]
    # reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard)
    # bot.send_message(chat_id=chat_id, text=message, reply_markup = reply_markup) 
    bot.send_message(chat_id=chat_id, text=message)


# /all_house_letters
def all_house_letters(bot, update):
    chat_id = update.message.chat_id
    if (chatDB.is_chat_registered(chat_id)):
        message = ""
        for house in HOUSES:
            letters = houseDB.get_house_letters(house)
            message = message + house + ":\n" + ", ".join(letters) + "\n"

        # Logger
        house = chatDB.get_house(chat_id)
        logger.info("%s from Team %s wants to view the letters from all the houses.", update.message.from_user.first_name, house)
    else:
        message = "Chat not registered yet."

    bot.send_message(chat_id=chat_id, text=message) #database


# ========= end ==========


# Registers command in the dispatcher
def registerCommand(dispatcher, commandStr, callback):
        handler = CommandHandler(commandStr, callback)
        dispatcher.add_handler(handler)

