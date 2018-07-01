from HouseDBHelper import HouseDBHelper
from ChatDBHelper import ChatDBHelper
from StationDBHelper import StationDBHelper

global houseDB
houseDB = HouseDBHelper()
houseDB.setup()

global chatDB
chatDB = ChatDBHelper()
chatDB.setup()

global stationDB
stationDB = StationDBHelper()
stationDB.setup()


