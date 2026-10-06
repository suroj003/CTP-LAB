import sqlite3


class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY,
            name TEXT,
            designation TEXT,
            department TEXT,
            salary REAL
        )
        """)

        self.con.commit()

    def create(self):
        eid = int(input("Enter employee id: "))
        name = input("Enter name: ")
        des = input("Enter designation: ")
        dept = input("Enter department: ")
        salary = float(input("Enter salary: "))

        self.cur.execute(
            "INSERT INTO employee VALUES (?, ?, ?, ?, ?)",
            (eid, name, des, dept, salary)
        )

        self.con.commit()
        print("Employee added")

    def read(self):
        self.cur.execute("SELECT * FROM employee")

        for emp in self.cur.fetchall():
            print(emp)

    def update(self):
        eid = int(input("Enter employee id: "))
        salary = float(input("Enter new salary: "))

        self.cur.execute(
            "UPDATE employee SET salary = ? WHERE id = ?",
            (salary, eid)
        )

        self.con.commit()
        print("Employee updated")

    def delete(self):
        eid = int(input("Enter employee id: "))

        self.cur.execute(
            "DELETE FROM employee WHERE id = ?",
            (eid,)
        )

        self.con.commit()
        print("Employee deleted")


obj = Employee()

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        obj.create()
    elif ch == 2:
        obj.read()
    elif ch == 3:
        obj.update()
    elif ch == 4:
        obj.delete()
    elif ch == 5:
        break
    else:
        print("Wrong choice")