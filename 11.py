import numpy as np


class Matrix:
    def __init__(self):
        self.a = np.array([
            [1, 2, 3],
            [0, 1, 4],
            [5, 6, 0]
        ])

    def calculate(self):
        determinant = np.linalg.det(self.a)
        inverse = np.linalg.inv(self.a)
        rank = np.linalg.matrix_rank(self.a)

        print("Matrix:")
        print(self.a)

        print("\nDeterminant =", round(determinant, 2))

        print("\nInverse:")
        print(inverse)

        print("\nRank =", rank)


obj = Matrix()
obj.calculate()