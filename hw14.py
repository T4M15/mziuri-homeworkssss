import math

#1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 2500:
            print("You cannot deposit more than 2500 GEL at once.")
        elif amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"{amount} GEL deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(" GEL withdrawn successfully.")

    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Current balance: {self.balance} GEL")


#2

class Shape:
    def describe(self):
        print("I am a shape")


class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(sides=3)
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area



account = BankAccount("Giorgi", 1000)
account.deposit(2000)
account.deposit(3000)
account.withdraw(500)
account.withdraw(5000)
account.display_balance()

print("------------")


triangle = Triangle(3, 4, 5)
triangle.describe()
print("Triangle area:", triangle.calculate_area())