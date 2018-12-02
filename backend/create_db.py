import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

# Create users table
c.execute('''CREATE TABLE users (
                  user_id INTEGER PRIMARY KEY,
                  name text NOT NULL
              )''')

# Create restriction table
c.execute('''CREATE TABLE restrictions (
                  restriction_id INTEGER PRIMARY KEY,
                  name text NOT NULL,
                  type text NOT NULL
              )''')

# Create ingred_restriction table
c.execute('''CREATE TABLE ingred_restricts (
                  ingred_restrict_id INTEGER PRIMARY KEY,
                  restriction_id INTEGER NOT NULL,
                  amount text NOT NULL
              )''')

# Create nutri_restriction table
c.execute('''CREATE TABLE nutri_restricts (
                  nutri_restrict_id INTEGER PRIMARY KEY,
                  restriction_id INTEGER NOT NULL,
                  amount text NOT NULL
              )''')

# Create consumptions table
c.execute('''CREATE TABLE consumptions (
                  consumption_id INTEGER PRIMARY KEY,
                  user_id INTEGER NOT NULL,
                  ingreds text NOT NULL,
                  nutrients text NOT NULL,
                  date text NOT NULL
              )''')

# Create fooditem table
c.execute('''CREATE TABLE food (
                  food_id INTEGER PRIMARY KEY,
                  name text NOT NULL
              )''')

# Create ingredients table
c.execute('''CREATE TABLE ingredients (
                  ingred_id INTEGER PRIMARY KEY,
                  food_id INTEGER NOT NULL,
                  name text NOT NULL,
                  amount text NOT NULL
              )''')

# Create nutrients table
c.execute('''CREATE TABLE nutrients (
                  nutri_id INTEGER PRIMARY KEY,
                  food_id INTEGER NOT NULL,
                  name text NOT NULL,
                  amount text NOT NULL
              )''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


