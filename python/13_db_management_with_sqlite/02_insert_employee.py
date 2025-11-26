import sqlite3
# connect database and create database if it is not already exists
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Executing Query
cursor.execute('''
    INSERT INTO employees(name, age, department)
    VALUES(?,?,?)
''', ("John",26,"Development"))
conn.commit()
conn.close()
print("Employee inserted successfully!")