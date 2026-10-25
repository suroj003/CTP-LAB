
import xml.etree.ElementTree as ET

tree = ET.parse("university_records.xml")
root = tree.getroot()

print("University:", root.get("name"))
print("=" * 60)

for campus in root.findall("campus"):
    print("Location:", campus.findtext("location"))
    print("Established:", campus.findtext("established"))
    print("Website:", campus.findtext("website"))

for department in root.findall("./departments/department"):
    print("\nDepartment:", department.findtext("name"))
    print("Department ID:", department.get("id"))
    print("HOD:", department.findtext("hod"))
    print("Building:", department.findtext("building"))

    for student in department.findall("./students/student"):
        print("\nStudent ID:", student.get("id"))

        personal = student.find("personal_details")
        academic = student.find("academic_details")

        name = personal.find("name")
        print("Name:", name.findtext("first_name"),
              name.findtext("last_name"))

        print("Gender:", personal.findtext("gender"))
        print("Email:", personal.findtext("email"))

        address = personal.find("address")
        print("City:", address.findtext("city"))
        print("State:", address.findtext("state"))

        print("\nAcademic Details:")
        print("Year:", academic.findtext("year"))
        print("Semester:", academic.findtext("semester"))
        print("CGPA:", academic.findtext("cgpa"))
        print("Advisor:", academic.findtext("advisor"))

        print("\nCourses:")
        for course in academic.findall("./courses/course"):
            print("Course:", course.findtext("name"))
            print("Code:", course.get("code"))
            print("Credits:", course.findtext("credits"))
            print("Marks:", course.findtext("marks"))
            print("Grade:", course.findtext("grade"))
            print("-" * 30)

    print("=" * 60)
