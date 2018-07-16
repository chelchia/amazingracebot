import sqlite3
from stationInfo import NUM_OPTIONAL_STATIONS

# Database: stationDB.sqlite
# Table: stations
# Columns: stn_number, letters_left

NUM_OPTIONAL_STATIONS = 11
DEFAULT_REDEMPTIONS = 3

class StationDBHelper:
    def __init__(self, dbname="stationDB.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        self.cur = self.conn.cursor()

    def setup(self):
        self.conn.execute("DROP TABLE IF EXISTS stations") #(for testing purposes)
        print("creating stations table (if it does not exist)")
        stmt = "CREATE TABLE IF NOT EXISTS stations (stn_number integer, letters_left integer)"
        self.conn.execute(stmt)
        self.conn.commit()

        for stn in range(1, NUM_OPTIONAL_STATIONS + 1):
            stmt = "INSERT INTO stations VALUES (?, ?)"
            args = (stn, DEFAULT_REDEMPTIONS,)
            self.conn.execute(stmt, args)
            self.conn.commit()

    def decrease_letter_count(self, station):
        letter_count = self.get_letters_left(station) - 1
        stmt = "UPDATE stations SET letters_left=(?) WHERE stn_number=(?)"
        args = (letter_count, station, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_letters_left(self, station):
        stmt = "SELECT letters_left FROM stations WHERE stn_number = (?)"
        args = (station,)
        self.cur.execute(stmt, args)
        entry = self.cur.fetchone()
        return entry[0]

