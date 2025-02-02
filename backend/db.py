import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
conn.commit()
