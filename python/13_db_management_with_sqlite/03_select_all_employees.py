import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Fetch records query
cursor.execute("SELECT*from employees")
rows=cursor.fetchall()

for row in rows:
    print(row[3])

conn.close()