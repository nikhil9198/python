import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Get employee id from user
emp_id=int(input("Enter a employee id to update:  "))

# Get department from employee to update
new_dept=input("Enter the new dep: ")

# SQLite query to update
cursor.execute("UPDATE employees SET department = ? WHERE id = ? ",(new_dept,emp_id))

# Commit Changes\
conn.commit()

# Printing Successful massage
print("Employee Updated successfully")
# Close the connection
conn.close()