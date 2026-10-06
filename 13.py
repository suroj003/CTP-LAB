from scipy.integrate import quad
from scipy.optimize import approx_fprime


class Calculator:
    def function(self, x):
        return x ** 2 + 3 * x + 2

    def calculate(self):
        x = 2
        h = 0.0001

        d = (self.function(x + h) - self.function(x - h)) / (2 * h)

        result, error = quad(self.function, 0, 2)

        print("Differentiation =", d)
        print("Integration =", result)


obj = Calculator()
obj.calculate()