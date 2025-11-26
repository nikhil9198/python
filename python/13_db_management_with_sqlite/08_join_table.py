import sqlite3

# Connecting with existing database
conn=sqlite3.connect("company.db")
cursor=conn.cursor()

# Create projects table

cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_id INTEGER,
    project_name TEXT,
    FOREIGN KEY (emp_id) REFERENCES employees(id)
    )
''')

# Insert projects data
# cursor.execute("INSERT INTO projects (emp_id,project_name) VALUES(?,?)",(10,"Requirement Gathering"))
# print("New record has been added successfully")

# Joining tables and fetching combined data
cursor.execute('''
    SELECT employees.name, employees.age, projects.project_name FROM employees INNER JOIN projects ON employees.id=projects.emp_id
''')
rows=cursor.fetchall()

# loop through all records
for row in rows:
    print(row)

# Saving the change
conn.commit()

# Close connection
conn.close()