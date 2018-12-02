import sqlite3

class DbHandler(object):
    def __init__(self, dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.c = self.conn.cursor()

    def add_user(self, user_name):
        query = "INSERT INTO users (name) VALUES ('{}')".format(user_name)
        self.c.execute(query)
        self.conn.commit()

    def add_restriction(self, r_name, r_type):
        query = "INSERT INTO restrictions (name, type) VALUES ('{}', '{}')".format(r_name, r_type)
        self.c.execute(query)
        self.conn.commit()

    def add_consumption(self, user_id, ingred, nutri):
        date = 0 #TODO get datetime
        query = "INSERT INTO restrictions (user_id, ingreds, nutrients, date) VALUES ('{}', '{}')".format(user_id, ingred, nutri, date)
        self.c.execute(query)

        #Add food item to fooditem table
        self.conn.commit()

    def get_consumption(self, user_name):
        query = "SELECT * FROM consumptions WHERE user_id IS WHERE user_id IS (SELECT user_id FROM users WHERE name IS {})".format(user_name)
        result = self.c.execute(query)
        consum = result.fetchone()[0]
        return consum

    
