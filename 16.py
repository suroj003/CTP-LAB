import sqlite3


class Student:
    def __init__(self):
        self.con = sqlite3.connect("student.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            cgpa REAL
        )
        """)

        self.con.commit()

    def insert(self):
        roll = int(input("Enter roll no: "))
        name = input("Enter name: ")
        dept = input("Enter department: ")
        cgpa = float(input("Enter CGPA: "))

        self.cur.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, dept, cgpa)
        )

        self.con.commit()
        print("Student added")

    def display(self):
        self.cur.execute("SELECT * FROM students")

        data = self.cur.fetchall()

        for student in data:
            print(student)

    def search(self):
        roll = int(input("Enter roll no: "))

        self.cur.execute(
            "SELECT * FROM students WHERE roll = ?",
            (roll,)
        )

        student = self.cur.fetchone()

        if student:
            print(student)
        else:
            print("Student not found")


obj = Student()

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Search")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        obj.insert()
    elif ch == 2:
        obj.display()
    elif ch == 3:
        obj.search()
    elif ch == 4:
        break
    else:
        print("Wrong choice")