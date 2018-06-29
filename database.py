from HouseDBHelper import HouseDBHelper
from ChatDBHelper import ChatDBHelper

global houseDB
houseDB = HouseDBHelper()
houseDB.setup()

# mychange 
global chatDB
chatDB = ChatDBHelper()
chatDB.setup()


#def addLetter(bot, update):
#	text = update.message.text
#	houseDB.add_letter("TRITON", text)
#	houseDB.add_letter("IANTHE", text)

