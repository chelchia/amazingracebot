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
		return "Key Station " + str(self.number) + ": " + self.location + "\nLetters: " + self.print_letters() + "\n"


# Dictionary of stations
stations = {}

num = 1
instruction = "instructions 1"
location = "location 1"
letters = ['Z']
password = "password1"
station = Station(num, instruction, location, letters, password)
stations[num] = station

num = 2
instruction = "instructions 2"
location = "location 2"
letters = ['X', 'Y']
password = "password2"
station = Station(num, instruction, location, letters, password)
stations[num] = station




# === Key stations ===
keyStations = {}

num = 'A'
location = "MPSH 1"
letters = ['A', 'E']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'B'
location = "YIH wooden open area (beside subway)"
letters = ['B', 'F']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'C'
location = "Central library"
letters = ['C', 'G']
station = KeyStation(num, location, letters)
keyStations[num] = station

num = 'D'
location = "Outside LT27, Science"
letters = ['D', 'H']
station = KeyStation(num, location, letters)
keyStations[num] = station


key_station_passwords = {
	'winA': ['A'],
	'loseA': ['E'],
	'winB': ['B']
}







