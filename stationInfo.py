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


# Dictionary of stations
stations = {}

num = 1
instruction = "instructions 1"
location = "location 1"
letters = ['A', 'B']
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











