import sqlite3

def get_connection():
    conn = sqlite3.connect("employee_management.db")
    cursor = conn.cursor()
    return conn, cursor
def create_tables():
    conn, cursor=get_connection()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id INTEGER,
            project_name TEXT,
            FOREIGN KEY(emp_id) REFERENCES employees(id)
            )
        ''')
    conn.commit()
    conn.close()

def add_employee():
    name=input("enter employee name: ")
    age=int(input("enter employee age: "))
    dept=input("enter employee department: ")

    conn, cursor = get_connection()
    cursor.execute()