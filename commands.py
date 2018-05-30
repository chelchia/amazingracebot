import telegram
from telegram.ext import CommandHandler
from qrcodeHandler import qrcodeHandler

# ===== Bot commands ===== 

# /start
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Started chat with amazing race bot.")

# /station
def station(bot, update):
	# bot.send_message(chat_id=update.message.chat_id, text="Send me a pic of the qr code. Text 'cancel' to cancel.")
	# reply = bot.get_updates() #PROBLEM: get updates too soon, doesnt get the correct update
	# while (true):
	# 	reply = bot.get_updates()
	# 	if (reply != []):
	# 		break
	# qrcodeHandler(bot, reply)
	forceReplyObj = telegram.ForceReply(force_reply=True, selective=False)
	bot.send_message(chat_id=update.message.chat_id, text="Send me a pic of the qr code.", reply_markup=forceReplyObj)


# ========= end ==========


# Registers command in the dispatcher
def registerCommand(dispatcher, commandStr, callback):
	handler = CommandHandler(commandStr, callback)
	dispatcher.add_handler(handler)
