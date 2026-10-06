import sqlite3


class SalaryReport:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()

    def report(self):
        dept = input("Enter department: ")

        self.cur.execute("""
        SELECT department, COUNT(*), SUM(salary), AVG(salary)
        FROM employee
        WHERE department = ?
        GROUP BY department
        """, (dept,))

        data = self.cur.fetchone()

        if data:
            print("\nDepartment:", data[0])
            print("Number of employees:", data[1])
            print("Total salary:", data[2])
            print("Average salary:", data[3])
        else:
            print("Department not found")


obj = SalaryReport()
obj.report()