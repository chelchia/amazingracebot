import sqlite3

# Database: chatDB.sqlite
# Table: houses
# Columns: chat_id, house

class ChatDBHelper:
    def __init__(self, dbname="chatDB.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread = False)
        self.c = self.conn.cursor()

    def setup(self):
        # self.conn.execute("DROP TABLE IF EXISTS houses ") #(for testing purposes)
        print("creating chat_id/house table (if it does not exist)")
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
        stmt = "SELECT house from houses"
        registered = [x[0] for x in self.conn.execute(stmt)]
        for h in registered:
            print(h + "\n")
        if house in registered:
            print("REGISTERED!")
            return True
        else:
            print("NOT REGISTERED!")
            return False
    
    def remove_chat(self, chat_id):
        stmt = "DELETE FROM houses WHERE chat_id = (?)"
        args = (chat_id, )
        self.c.execute(stmt, args)
        self.conn.commit()

    def print_table(self):
        # stmt = "SELECT * FROM houses"
        # table = self.c.execute(stmt)
        # print(table)
        # self.c.execute("SELECT * FROM houses")
        rows = self.c.fetchall()
        for row in rows:
            print(row)
