import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Get input from user
dept=input("Enter department to search employees: ")
# Filter by age
# cursor.execute("SELECT*FROM employees WHERE department =?",(dept,))
cursor.execute("SELECT*FROM employees WHERE department LIKE ?",('%' +dept+ '%',))
rows=cursor.fetchall()

for row in rows:
    print(row)

conn.close()