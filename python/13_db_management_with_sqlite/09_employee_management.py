import sqlite3

from pycparser.c_ast import While


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
    cursor.execute("INSERT INTO employees(name, age, department) VALUES(?,?,?)", (name, age, dept))
    conn.commit()
    conn.close()
    print("Employee Added Successfully!")

def view_employee():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM employees")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def search_by_department():
    dept=input("Enter department to search: ")
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM employees WHERE department=?", (dept,))
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def update_department():
    emp_id=int(input("Enter Employee ID to Update: "))
    new_dept=input("Enter new department: ")
    conn, cursor = get_connection()
    cursor.execute("UPDATE employees SET department=? WHERE id=?", (new_dept,emp_id))
    conn.commit()
    conn.close()
    print("Employee Updated successfully!")

def delete_employee():
    emp_id=(input("Enter Employee ID to Delete: "))
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM employees WHERE id=?",(emp_id,))
    conn.commit()
    conn.close()
    print("Employee Deleted successfully!")

def assign_project():
    emp_id=(input("Enter Employee ID: "))
    project=input("Enter project name: ")
    conn, cursor = get_connection()
    cursor.execute("INSET INTO projects (emp_id,project_name) VALUES(?,?)",(emp_id,project))
    conn.commit()
    conn.close()
    print("Project assign successfully!")

def view_employee_with_projects():
    conn, cursor = get_connection()
    cursor.execute('''
        SELECT employees.name, employees.department, projects.project
        FROM employees
        INNER JOIN projects ON employees.id = project.emp_id
    ''')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def menu():
    while True:
        print("===Employee Management System")
        print("1. Add new employee")
        print("2. View employees")
        print("3. Search by Department")
        print("4. Update department")
        print("5. Delete employees")
        print("6. Assign projects")
        print("7. View Employees with projects")
        print("0. Exit")

        choice=input("Enter your choice: ")
        print()

        if choice=='1':
            add_employee()
        elif choice=='2':
            view_employee()
        elif choice=='3':
            search_by_department()
        elif choice=='4':
            update_department()
        elif choice=='5':
            delete_employee()
        elif choice=='6':
            assign_project()
        elif choice=='7':
            view_employee_with_projects()
        elif choice=='0':
            print("Exiting Program GoodByy!")
        else:
            print("Invalid Choice. Please try again\n")

if __name__=="__main__":
    menu()