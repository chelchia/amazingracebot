import requests
import telegram
from telegram.ext import (Updater, MessageHandler, Filters, ConversationHandler, CommandHandler, RegexHandler)

from settings import token
from commands import *
from stationInfo import all_password_regex


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
            CONFIRMATION_REQUEST: [RegexHandler('^(Ilykoie|Neo|Laventus|Oneiroi|Alerion|Rabanna)$', registerHouse)],
            },
        fallbacks=[CommandHandler('remove', remove), CommandHandler('cancel', cancel)]
        )
dispatcher.add_handler(start_conv_handler)

# 'Play' conversation handler -- output station instructions
play_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            CONFIRMATION_REQUEST: [RegexHandler('^(1|2|3|4|5|6|7|8|9|10)$', get_instructions)],
            },
        fallbacks=[CommandHandler('cancel', cancel)]
        )
dispatcher.add_handler(play_conv_handler)


# Message handler for station completion
completion_handler = RegexHandler(all_password_regex, station_complete)
dispatcher.add_handler(completion_handler)


# Polling for updates
updater.start_polling()

updater.idle()
