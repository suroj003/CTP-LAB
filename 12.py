import numpy as np


class Eigen:
    def __init__(self):
        self.a = np.array([
            [4, 1],
            [2, 3]
        ])

    def calculate(self):
        values, vectors = np.linalg.eig(self.a)

        print("Matrix:")
        print(self.a)

        print("\nEigenvalues:")
        print(values)

        print("\nEigenvectors:")
        print(vectors)


obj = Eigen()
obj.calculate()