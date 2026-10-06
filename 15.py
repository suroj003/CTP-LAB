from scipy.optimize import minimize


class Function:
    def calculate(self, xy):
        x = xy[0]
        y = xy[1]

        return (x - 2) ** 2 + (y - 2) ** 2


obj = Function()

start = [0, 0]

result = minimize(obj.calculate, start)

print("Minimum value =", result.fun)
print("x =", result.x[0])
print("y =", result.x[1])