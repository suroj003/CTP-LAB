import numpy as np


class Matrix:
    def __init__(self):
        self.a = [[1, 2], [3, 4]]
        self.b = [[5, 6], [7, 8]]

    def without_numpy(self):
        print("Without NumPy")

        add = [[0, 0], [0, 0]]
        sub = [[0, 0], [0, 0]]
        mul = [[0, 0], [0, 0]]

        for i in range(2):
            for j in range(2):
                add[i][j] = self.a[i][j] + self.b[i][j]
                sub[i][j] = self.a[i][j] - self.b[i][j]

        for i in range(2):
            for j in range(2):
                for k in range(2):
                    mul[i][j] += self.a[i][k] * self.b[k][j]

        trans = [[self.a[j][i] for j in range(2)] for i in range(2)]

        print("Addition:", add)
        print("Subtraction:", sub)
        print("Multiplication:", mul)
        print("Transpose:", trans)

    def using_numpy(self):
        a = np.array(self.a)
        b = np.array(self.b)

        print("\nUsing NumPy")
        print("Addition:\n", a + b)
        print("Subtraction:\n", a - b)
        print("Multiplication:\n", np.dot(a, b))
        print("Transpose:\n", a.T)


obj = Matrix()

obj.without_numpy()
obj.using_numpy()