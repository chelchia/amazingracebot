import sqlite3

class DBHelper:

    def __init__(self, dbname="amazingRace.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread = False)
        self.c = self.conn.cursor()

    def setup(self):
        print("creating chat_id/house table (if it does not exits)")
        houses_table = "CREATE TABLE IF NOT EXISTS houses (chat_id text, house text)"
        self.c.execute(houses_table)
        self.conn.commit()

    def add_house(self, chat_id, house):
        stmt = "INSERT INTO houses (chat_id, house) VALUES (?, ?)"
        args = (chat_id, house)
        self.c.execute(stmt, args)
        self.conn.commit()

    def get_house(self, chat_id):
        stmt = "SELECT house FROM houses WHERE chat_id = (?)"
        args = (chat_id,)
        # return [x for x in self.conn.execute(stmt, args)]
        row = self.c.execute(stmt, args).fetchone()
        return row[0]

    def is_house_registered(self, house):
        stmt = "SELECT COUNT(*) FROM houses WHERE house = (?)"
        args = (house,)
        if  self.c.execute(stmt, args) == 0:
            return True
        else:
            return False
