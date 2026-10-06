import numpy as np


class StudentMarks:
    def __init__(self):
        self.mid = np.array([
            [65, 70, 68, 72],
            [78, 75, 80, 77],
            [55, 60, 58, 62],
            [82, 85, 80, 88],
            [70, 68, 72, 74]
        ])

        self.end = np.array([
            [72, 78, 75, 80],
            [84, 82, 86, 83],
            [65, 68, 66, 70],
            [88, 90, 85, 92],
            [78, 75, 80, 82]
        ])

    def calculate(self):
        mid_total = np.sum(self.mid, axis=1)
        end_total = np.sum(self.end, axis=1)

        mid_avg = np.mean(self.mid, axis=1)
        end_avg = np.mean(self.end, axis=1)

        improvement = ((end_total - mid_total) / mid_total) * 100

        print("Student  Mid Total  End Total  Mid Avg  End Avg  Improvement")

        for i in range(5):
            print(
                "S" + str(i + 1),
                "   ",
                mid_total[i],
                "      ",
                end_total[i],
                "      ",
                round(mid_avg[i], 2),
                "    ",
                round(end_avg[i], 2),
                "    ",
                round(improvement[i], 2), "%"
            )


obj = StudentMarks()
obj.calculate()