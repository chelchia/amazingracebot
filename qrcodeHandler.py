import telegram
from telegram.ext import MessageHandler, Filters


def decodeQRcode(bot, update):
	print(update.message)
	bot.send_message(chat_id=update.message.chat_id, text="station received")

qrcodeHandler = MessageHandler(Filters.photo & Filters.reply, decodeQRcode)
