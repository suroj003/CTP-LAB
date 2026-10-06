class Course:
    def __init__(self):
        self.s1 = {"Python", "DBMS", "Maths"}
        self.s2 = {"Python", "OS", "Maths"}

        self.st1 = ("S1", "Rahul", 101)
        self.st2 = ("S2", "Aman", 102)

    def show(self):
        print("Student 1 details:", self.st1)
        print("Student 2 details:", self.st2)

        print("\nCourses of Student 1:", self.s1)
        print("Courses of Student 2:", self.s2)

        print("\nCommon courses:", self.s1.intersection(self.s2))

        print("Courses only in Student 1:", self.s1.difference(self.s2))

        print("Courses only in Student 2:", self.s2.difference(self.s1))

        print("All courses:", self.s1.union(self.s2))


obj = Course()
obj.show()