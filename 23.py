import xml.etree.ElementTree as ET

tree = ET.parse("student.xml")
root = tree.getroot()

# Display student details
for student in root.findall("student"):
    print(student.find("name").text,
          student.find("department").text)

# Add a new student
s = ET.SubElement(root, "student", id="111")
ET.SubElement(s, "name").text = "Ravi Das"
ET.SubElement(s, "department").text = "CSE"
ET.SubElement(s, "year").text = "2"
ET.SubElement(s, "email").text = "ravi@example.com"
ET.SubElement(s, "cgpa").text = "8.5"

tree.write("student.xml")
print("Student added successfully")