import sqlite3
# connect database and create database if it is not already exists
conn=sqlite3.connect("company.db")
# print("Database connected successfully!")

# create a cursor to execute SQL command
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
department TEXT
)
''')

conn.commit()
conn.close()
print("Table created a successfully and connection closed!")