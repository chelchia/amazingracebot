import telegram
from telegram.ext import CommandHandler
from database import houseDB

HOUSES = ("URSAIA", "NOCTURNA", "IANTHE", "TRITON", "ANKAA", "SAREN")

# ===== Bot commands ===== 
# /start
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Started chat with amazing race bot.")

# /station
def station(bot, update):
	# forceReplyObj = telegram.ForceReply(force_reply=True, selective=False)
	# bot.send_message(chat_id=update.message.chat_id, text="Send me a pic of the qr code.", reply_markup=forceReplyObj)
	bot.send_message(chat_id=update.message.chat_id, text="Station.")

# /my_house_letters
def my_house_letters(bot, update):
	# house = getHouse() #TODO
	letters = houseDB.get_house_letters("TRITON") #TODO: work with yaofeng on house and chatid
	message = "TRITON" + ":\n" + "\n".join(letters)
	bot.send_message(chat_id=update.message.chat_id, text=message) #database

# /all_house_letters
def all_house_letters(bot, update):
	message = ""
	for house in HOUSES:
		letters = houseDB.get_house_letters(house)
		message = message + house + ":\n" + ", ".join(letters) + "\n"
	bot.send_message(chat_id=update.message.chat_id, text=message) #database


# ========= end ==========


# Registers command in the dispatcher
def registerCommand(dispatcher, commandStr, callback):
	handler = CommandHandler(commandStr, callback)
	dispatcher.add_handler(handler)


