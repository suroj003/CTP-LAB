import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


class Polynomial:
    def function(self, x, a, b, c):
        return a * x ** 2 + b * x + c

    def calculate(self):
        x = np.array([1, 2, 3, 4, 5, 6])
        y = np.array([6, 17, 34, 57, 86, 121])

        values, extra = curve_fit(self.function, x, y)

        a, b, c = values

        print("Polynomial coefficients:")
        print("a =", a)
        print("b =", b)
        print("c =", c)

        print("\nPolynomial:")
        print("y =", round(a, 2), "x^2 +", round(b, 2), "x +", round(c, 2))

        new_x = np.linspace(1, 6, 100)
        new_y = self.function(new_x, a, b, c)

        plt.scatter(x, y, label="Original Data")
        plt.plot(new_x, new_y, label="Fitted Curve")

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Second Degree Polynomial Fit")
        plt.legend()
        plt.show()


obj = Polynomial()
obj.calculate()