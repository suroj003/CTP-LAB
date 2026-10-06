class Number:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        fact = 1
        for i in range(1, self.n + 1):
            fact = fact * i
        return fact

    def prime(self):
        if self.n < 2:
            return False

        for i in range(2, self.n):
            if self.n % i == 0:
                return False
        return True


n = int(input("Enter a number: "))

obj = Number(n)

print("Factorial =", obj.factorial())

if obj.prime():
    print("Number is Prime")
else:
    print("Number is not Prime")