import telegram
from telegram.ext import (CommandHandler, ConversationHandler, RegexHandler)
from database import houseDB
from databaseYF import DBHelper
db = DBHelper()
db.setup()

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
    reply_keyboard = [['Ursaia'], ['Nocturna'], ['Ianthe'], ['Triton'], ['Ankaa'], ['Saren']]
    reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(text="Please Choose Your House!", reply_markup = reply_markup)
    return CONFIRMATION_REQUEST


# This method should be automatically called after the user enters their house.
# Evaluates whether that house is already registered in our database or not
# It it is, the bot will output "What! Wanna check again?! (Type '/start' to choose another house)" 
# Else, the bot will add the chat id and the house into our database and output " AWESOME! <name of house> will be my favourite house now!" 
def registerHouse(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    if (db.is_house_registered(text)):
        update.message.reply_text(text = "What! Wanna check again?! Type '/start' to choose another house", reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        db.add_house(chat_id, text)
        logger.info("Team %s has been registered by %s.", text, update.message.from_user.first_name)
        update.message.reply_text(text = "AWESOME! Team {} will be my favourite house now!".format(text), reply_markup=telegram.ReplyKeyboardRemove())
        reply_keyboard = [["/my_house_letters", "/all_house_letters"]]
        reply_markup = telegram.ReplyKeyboardMarkup(reply_keyboard)
        house = db.get_house(chat_id)
        bot.sendMessage(chat_id=chat_id,text = "Press '/my_house_letters' to see the letter(s) Team {} has collected.\n\nPress '/all_house_letters' to see the letter(s) that other houses have collected.".format(house), replymark_up=reply_markup)
# /cancel
# Just in case, the user does not wants to register a house
def cancel(bot, update):
    update.message.reply_text(":'(")


# /station
def station(bot, update):
    # forceReplyObj = telegram.ForceReply(force_reply=True, selective=False)
        # bot.send_message(chat_id=update.message.chat_id, text="Send me a pic of the qr code.", reply_markup=forceReplyObj)
        bot.send_message(chat_id=update.message.chat_id, text="Station.")


# /my_house_letters
def my_house_letters(bot, update):
    chat_id = update.message.chat_id
    house = db.get_house(chat_id)
    logger.info("%s from Team %s wants to view their letters.", update.message.from_user.first_name, house)
    letters = houseDB.get_house_letters(house) 
    message = house + ":\n" + "\n".join(letters)
    bot.send_message(chat_id=chat_id, text=message) 

# /all_house_letters
def all_house_letters(bot, update):
        chat_id = update.message.chat_id
        house = db.get_house(chat_id) 
        message = ""
        for house in HOUSES:
                letters = houseDB.get_house_letters(house)
                message = message + house + ":\n" + ", ".join(letters) + "\n"
        bot.send_message(chat_id=chat_id, text=message) #database
        logger.info("%s from Team %s wants to view the letters from all the houses.", update.message.from_user.first_name, house)


# ========= end ==========

# Registers command in the dispatcher
def registerCommand(dispatcher, commandStr, callback):
        handler = CommandHandler(commandStr, callback)
        dispatcher.add_handler(handler)

