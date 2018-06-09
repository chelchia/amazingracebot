from DBHelper import DBHelper

global db
db = DBHelper()
db.setup()

#WORKS FINE
# db.add_item("hi")
# items = db.get_items()
# message = "\n".join(items)
# print("messsage: " + message)

def addWithMessage(bot, update):
	# global db
	print("addWithMessage called")
	text = update.message.text
	bot.send_message(chat_id=update.message.chat_id, text=text)
	db.add_item("text")
	print("2")
	items = db.get_items()
	message = "\n".join(items)
	print("messsage: " + message)
	bot.send_message(chat_id=update.message.chat_id, text=message)

