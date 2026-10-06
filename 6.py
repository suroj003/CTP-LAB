class Student:
    def grade(self, avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def process(self):
        fin = open("6_students.txt", "r")
        fout = open("6_result.txt", "w")

        for line in fin:
            data = line.split()

            roll = data[0]
            name = data[1]

            marks = []
            for i in range(2, 6):
                marks.append(int(data[i]))

            total = sum(marks)
            avg = total / 4
            grade = self.grade(avg)

            fout.write(
                roll + " " + name +
                " Total=" + str(total) +
                " Average=" + str(avg) +
                " Grade=" + grade + "\n"
            )

        fin.close()
        fout.close()

        print("Result written in result.txt")


obj = Student()
obj.process()