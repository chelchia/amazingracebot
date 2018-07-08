import sqlite3

# Database: chatDB.sqlite
# Table: house_group_chats
# Columns: chat_id, house

class ChatDBHelper:
    def __init__(self, dbname="chatDB.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread = False)
        self.c = self.conn.cursor()

    def setup(self):
        self.conn.execute("DROP TABLE IF EXISTS house_group_chats ") #(for testing purposes)
        print("creating chat_id/house table (if it does not exist)")
        houses_table = "CREATE TABLE IF NOT EXISTS house_group_chats (chat_id integer, house text)"
        self.c.execute(houses_table)
        self.conn.commit()

    def is_house_registered(self, house_name):
        stmt = "SELECT house from house_group_chats"
        registered = [x[0] for x in self.conn.execute(stmt)]
        if house_name in registered:
            return True
        else:
            return False

    def is_chat_registered(self, chat):
        stmt = "SELECT chat_id from house_group_chats"
        registered = [x[0] for x in self.conn.execute(stmt)]
        for h in registered:
            if chat == h:
                return True
        return False

    # === Setter ===
    def add_house(self, chat, house_name):
        stmt = "INSERT INTO house_group_chats (chat_id, house) VALUES (?, ?)"
        args = (chat, house_name)
        self.c.execute(stmt, args)
        self.conn.commit()

    def remove_chat(self, chat):
        stmt = "DELETE FROM house_group_chats WHERE chat_id = (?)"
        args = (chat, )
        self.c.execute(stmt, args)
        self.conn.commit()

    # === Getters ===
    def get_house(self, chat):
        stmt = "SELECT house FROM house_group_chats WHERE chat_id = (?)"
        args = (chat,)
        # return [x for x in self.conn.execute(stmt, args)]
        row = self.c.execute(stmt, args).fetchone()
        return row[0]


    def print_table(self):
        # stmt = "SELECT * FROM house_group_chats"
        # table = self.c.execute(stmt)
        # print(table)
        # self.c.execute("SELECT * FROM house_group_chats")
        rows = self.c.fetchall()
        for row in rows:
            print(row)
