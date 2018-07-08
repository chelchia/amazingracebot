import sqlite3

# Database: houseDB.sqlite
# Table: houseLetters
# Columns: house, letters

# Stores all letters collected by houses.
class HouseDBHelper:
    def __init__(self, dbname="houseDB.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)

    def setup(self):
        self.conn.execute("DROP TABLE IF EXISTS houseLetters") #(for testing purposes)
        print("creating houseLetters table (if it does not exist)")
        stmt = "CREATE TABLE IF NOT EXISTS houseLetters (house text, letters text)"
        self.conn.execute(stmt)
        #add indexing
        self.conn.execute("CREATE INDEX IF NOT EXISTS house_index ON houseLetters (house)")
        self.conn.commit()

    def add_letters(self, house_text, tuple):
        for letter in tuple:
            self.add_one_letter(house_text, letter)

    def add_one_letter(self, house_text, letter_text):
        stmt = "INSERT INTO houseLetters VALUES (?, ?)"
        args = (house_text, letter_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()
        print("added " + house_text + " letter " + letter_text)

    def get_house_letters(self, house_name):
        stmt = "SELECT letters FROM houseLetters WHERE house = (?)"
        args = (house_name,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def already_collected(self, house, letter):
        house_letters = self.get_house_letters(house)
        if letter in house_letters:
            return True
        else:
            return False

