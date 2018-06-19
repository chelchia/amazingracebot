import requests
import telegram
from telegram.ext import (Updater, MessageHandler, Filters, ConversationHandler, CommandHandler, RegexHandler)

# from settings import token
from commands import *
# from database import addLetter

#======= Edits from yaofeng =====
from databaseYF import DBHelper
db = DBHelper()

# Initialisation
bot = telegram.Bot("561039995:AAGwINDFUT-28gbMFaRkuVvsIP2BcnrSzYM")
updater = Updater("561039995:AAGwINDFUT-28gbMFaRkuVvsIP2BcnrSzYM")
dispatcher = updater.dispatcher

# Register commands
# registerCommand(dispatcher, "start", start)
registerCommand(dispatcher, "station", station)
registerCommand(dispatcher, "my_house_letters", my_house_letters)
registerCommand(dispatcher, "all_house_letters", all_house_letters)

# Add conversation handler

conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],

        states={

            CONFIRMATION_REQUEST: [RegexHandler('^(Ursaia|Nocturna|Ianthe|Triton|Ankaa|Saren)$', registerHouse)],

            },

        fallbacks= [CommandHandler('cancel', cancel)]
        )
dispatcher.add_handler(conv_handler)
    # === for testing purposes only. Adds a letter to triton and ianthe by texting ===
#DBHandler = MessageHandler(Filters.text, addLetter)
#dispatcher.add_handler(DBHandler)
#TODO: work with meena on station and letters
# ===

# Polling for updates
updater.start_polling()

updater.idle()
