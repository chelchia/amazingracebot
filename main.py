import requests
import telegram
from telegram.ext import Updater, MessageHandler, Filters

from settings import token
from commands import *
from qrcodeHandler import qrcodeHandler
from database import addWithMessage, db

# Initialisation
bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

# Register commands
registerCommand(dispatcher, "start", start)
registerCommand(dispatcher, "station", station)

# Set up database to contain letters for each station
DBHandler = MessageHandler(Filters.text, addWithMessage)
dispatcher.add_handler(DBHandler)

# Polling for updates
updater.start_polling()

updater.idle()