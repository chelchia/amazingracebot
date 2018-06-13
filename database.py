from DBHelper import DBHelper
from HouseDBHelper import HouseDBHelper

global houseDB
houseDB = HouseDBHelper()
houseDB.setup()

def addLetter(bot, update):
	text = update.message.text
	houseDB.add_letter("TRITON", text)
	houseDB.add_letter("IANTHE", text)

