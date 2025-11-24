import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Get employee ID using user input
emp_id=int(input("Enter a employee ID to delete: "))

# Delete Query
cursor.execute("DELETE FROM employees WHERE id = ?",(emp_id,))

cursor.execute("SELECT * FROM employees")
rows=cursor.fetchall()
for row in rows:
    print(row)

# Save the changes permanently by commiting
conn.commit()

# Print successful massage
print("Employee deleted successfully")

# Closing the connection
conn.close()