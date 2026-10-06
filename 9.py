import numpy as np


class Statistics:
    def __init__(self, data):
        self.data = data

    def using_numpy(self):
        arr = np.array(self.data)

        print("Using NumPy")
        print("Mean =", np.mean(arr))
        print("Median =", np.median(arr))
        print("Standard Deviation =", np.std(arr))
        print("Minimum =", np.min(arr))
        print("Maximum =", np.max(arr))

    def without_numpy(self):
        n = len(self.data)

        # mean
        mean = sum(self.data) / n

        # median
        a = sorted(self.data)

        if n % 2 == 0:
            median = (a[n // 2 - 1] + a[n // 2]) / 2
        else:
            median = a[n // 2]

        # standard deviation
        total = 0
        for x in self.data:
            total = total + (x - mean) ** 2

        sd = (total / n) ** 0.5

        print("\nWithout NumPy")
        print("Mean =", mean)
        print("Median =", median)
        print("Standard Deviation =", sd)
        print("Minimum =", min(self.data))
        print("Maximum =", max(self.data))


marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]
temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]
sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]

print("MARKS")
obj = Statistics(marks)
obj.using_numpy()
obj.without_numpy()

print("\nTEMPERATURE")
obj = Statistics(temperatures)
obj.using_numpy()
obj.without_numpy()

print("\nSALES")
obj = Statistics(sales)
obj.using_numpy()
obj.without_numpy()