class Fibonacci:
    def fib(self, n):
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    def series(self, n):
        for i in range(n):
            print(self.fib(i), end=" ")


n = int(input("Enter number of terms: "))

obj = Fibonacci()

print("Fibonacci Series:")
obj.series(n)