# All information regarding stations.

class Station:
	def __init__(self, num, instruction_text, location_text, letter_tuple, password_text):
		self.number = num
		self.instruction = instruction_text
		self.location = location_text
		self.letters = letter_tuple
		self.password = password_text

	def print_instructions(self):
		return "Station " + str(self.number) + ": " + self.instruction

	def print_letters(self):
		return ', '.join(self.letters)

	def print_station(self):
		return "Station " + str(self.number) + ": " + self.location + "\nLetters: " + self.print_letters() + "\n"

class KeyStation(Station):
	def __init__(self, num, location, letters):
		Station.__init__(self, num, "", location, letters, "")

	def print_station(self):
		return "*Key Station " + str(self.number) + ": " + self.location + "*\nLetters: " + self.print_letters() + "\n"


# Dictionary of stations
stations = {}

num = 1
instruction = """*Catch no ball*
The house must hit a paper ball 50 times with their elbows or feet ONLY without it touching the floor.
"""
location = "area outside MPSH 5"
letters = ['F']
password = "1TZfhZ"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 2
instruction = """*Music Whispers*
Houses pick 6 people, of which 5 people to wear earphones blasting music. The freshie without earphones will be the first in line. They are supposed to pass a long message down the line without shouting (normal voice). OGLs will receive several long messages before the race to tell the first freshie in line. At the end, OGLs will ask a question to the last freshie related to the details in the message. The house will play 3 rounds, each round with 5 different people. If the house answers with 2/3 rounds correctly, they succeed.
"""
location = "University Sports Centre area beside carpark"
letters = ['S', 'G']
password = "2vMp5s"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 3
instruction = """*on/off*
Split the house into equal halves (if there are an odd number of freshies one OGL joins). Line the house up, with one half behind the other. OGLs will call out numbers. Eg. 3 - the first 3 people in the line will squat and stand back up. 5 - the next 5 people in the line will do the same. The line wraps around such that the next person after the last person is the first person. Both lines will do the same (ie. the first 3 ppl in both the line in front and behind will squat). They have to get through the entire series of numbers without mistakes. 

The sequence is: 6, 11, 9, 2, 10, 1, 1, 13, 1, 9, 5, 18, 5, 12, 20, 9, 14, 1, 7, 2
"""
location = "University Sports Centre level 2 area beside rock climbing wall"
letters = ['A', 'X']
password = "3AwMQa"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 4
instruction = """*Telepathy*
5 freshies start off at the base of the staircase, numbered 1 to 5. They must shout out a number from 1-5 that is NOT their own, and also put up the number of fingers they shout (to help others in case they didn't hear the numbers clearly). If no other freshie shouts the number they have shouted, they can ascend the number of steps they have just shouted. Once a freshie has reached the top, another freshie can take his/her number and continue playing with the group. The goal is for the entire house to reach the top. (OGL help watch carefully, in case some freshies cant hear/see each other!)
"""
location = "AS8 staircase (behind CLB bus stop)"
letters = ['R', 'Y']
password = "4XjHFH"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 5
instruction = """*Jump Shot*
Take a jump shot! Everyone's legs must be in the air, and their jumps must be in ascending order of height. (ie. the first person jumps a little, the next person jumps more, ...)
"""
location = "CLB garden"
letters = ['N', 'J']
password = "5Pes5j"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 6
instruction = """*Guess the drink*\nIMPT: OGLs please check for any allergies before starting this game!!!
Send 5 freshies to buy mixed fruit drinks at the drinks stall (get 5 drinks). The other freshies in the house must guess the fruits in each drink correctly.
"""
location = "The Deck"
letters = ['U', 'Q']
password = "6Yw5aT"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 7
instruction = """*Rest up!*
Treat someone to ice cream! :)
"""
location = "Engin McDonalds"
letters = ['M']
password = "7rZm3u"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 8
instruction = """*House photo*
Form the name of your house and the letters USP with your bodies (not just hands!)
"""
location = "Science block letters"
letters = ['H']
password = "8fLX42"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 9
instruction = """*Price Tag*
The house must gather items whose total price adds to a specific number (eg. $187.60). The house can only send 2/3 freshies into COOP at a time to look at the prices of the items inside. Freshies must select items by taking pictures of their price tags. Each group of freshies can only spent 1 min in COOP before they are rotated out and the next group comes in. OGLs will total the prices at the end to check. Freshies must gather at least one of each items: Textbook, Earphones, Clothing, Plushie, Stationary
*IMPT:* OGLs must make sure freshies wait outside at the grass patch and not block the staircase/entrance of COOP. Freshies are not to shout in COOP.
"""
location = "Science COOP"
letters = ['O', 'Z', 'B']
password = "9mpX5t"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 10
instruction = """*Multiplier*
The house gathers in a circle. They must go round the circle counting from 1 to 60, but when they meet a multiple of the 3 OR a number containing the number drawn, they must say their house name instead. (eg. 10, 11, "neo", "neo", 14, "15") If anyone shouts wrongly the house must restart.
"""
location = "MD2 Foyers"
letters = ['L', 'P']
password = "10Xbs8"
station = Station(num, instruction, location, letters, password)
stations[num] = station



# === Key stations ===
keyStations = {}

num = 'A'
location = "MPSH 1"
letters = ['E', 'V']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'B'
location = "YIH wooden open area (beside subway)"
letters = ['T', 'C']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'C'
location = "Central library"
letters = ['I', 'W']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'D'
location = "Outside LT27, Science"
letters = ['D', 'K']
station = KeyStation(num, location, letters)
keyStations[num] = station


key_station_passwords = {
	'ee85Fz': ['E'],
	'V7qUXD': ['V'],
	'T9RSrV': ['T'],
	'cY4BrG': ['C'],
	'ie2rj2': ['I'],
	'WHaW9w': ['W'],
	'DbTz3D': ['D'],
	'kAp5Bn': ['K']
}







