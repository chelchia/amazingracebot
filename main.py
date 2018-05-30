import requests
import telegram
from telegram.ext import Updater

from settings import token
from commands import *
from qrcodeHandler import qrcodeHandler

# Initialisation
bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

# Register commands
registerCommand(dispatcher, "start", start)
registerCommand(dispatcher, "station", station)

# Add QRcode handler
dispatcher.add_handler(qrcodeHandler)

# Polling for updates
updater.start_polling()

updater.idle()