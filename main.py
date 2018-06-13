import requests
import telegram
from telegram.ext import Updater, MessageHandler, Filters

from settings import token
from commands import *
from database import addLetter

# Initialisation
bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

# Register commands
registerCommand(dispatcher, "start", start)
registerCommand(dispatcher, "station", station)
registerCommand(dispatcher, "my_house_letters", my_house_letters)
registerCommand(dispatcher, "all_house_letters", all_house_letters)


# === for testing purposes only. Adds a letter to triton and ianthe by texting ===
DBHandler = MessageHandler(Filters.text, addLetter)
dispatcher.add_handler(DBHandler)
#TODO: work with meena on station and letters
# ===

# Polling for updates
updater.start_polling()

updater.idle()