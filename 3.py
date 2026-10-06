class Student:
    def __init__(self):
        self.students = []

    def insert(self):
        roll = input("Enter roll no: ")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        data = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        self.students.append(data)
        print("Student inserted")

    def delete(self):
        roll = input("Enter roll no to delete: ")

        for student in self.students:
            if student["roll"] == roll:
                self.students.remove(student)
                print("Student deleted")
                return

        print("Student not found")

    def search(self):
        roll = input("Enter roll no to search: ")

        for student in self.students:
            if student["roll"] == roll:
                print(student)
                return

        print("Student not found")

    def display(self):
        for student in self.students:
            print(student)


obj = Student()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        obj.insert()
    elif ch == 2:
        obj.delete()
    elif ch == 3:
        obj.search()
    elif ch == 4:
        obj.display()
    elif ch == 5:
        break
    else:
        print("Wrong choice")