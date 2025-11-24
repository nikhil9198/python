import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Sort records with order by
cursor.execute("SELECT*FROM employees ORDER BY age DESC LIMIT 1,2")
rows=cursor.fetchall()

# loop through all employees
for row in rows:
    print(row)

conn.close()