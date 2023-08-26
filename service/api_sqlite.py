import sqlite3
from os import path

con = sqlite3.connect(path.join('service', 'store.db'))
cursor = con.cursor()
cursor.execute('''CREAT TABLE IF NOT EXIST basketMenu(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Last name TEXT,
                By father name TEXT
                )''')
con.commit()

