import requests
import telegram
from telegram.ext import (Updater, MessageHandler, Filters, ConversationHandler, CommandHandler, RegexHandler)

from settings import token
from commands import *


# Initialisation
bot = telegram.Bot(token)
updater = Updater(token)
dispatcher = updater.dispatcher

# Register commands
registerCommand(dispatcher, "my_house_letters", my_house_letters)
registerCommand(dispatcher, "all_house_letters", all_house_letters)
registerCommand(dispatcher, "station_overview", station_overview)
registerCommand(dispatcher, "help", help)

# 'Start' conversation handler -- register house with bot
start_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CONFIRMATION_REQUEST: [RegexHandler('^(Ursaia|Nocturna|Ianthe|Triton|Ankaa|Saren)$', registerHouse)],
            },
        fallbacks=[CommandHandler('remove', remove), CommandHandler('cancel', cancel)]
        )
dispatcher.add_handler(start_conv_handler)

# 'Play' conversation handler -- output station instructions
play_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            CONFIRMATION_REQUEST: [MessageHandler(Filters.text, get_instructions)],
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        )
dispatcher.add_handler(play_conv_handler)


# Message handler for station completion
completion_handler = MessageHandler(Filters.text, station_complete)
dispatcher.add_handler(completion_handler)


# Polling for updates
updater.start_polling()

updater.idle()
