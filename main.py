class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")


class Shape:
    def area(self):
        print("Area is unknown")

class Square(Shape):
    def area(self):
        print("Square area:", 4 * 4)

class Circle(Shape):
    def area(self):
        print("Circle area:", 3.14 * 5 * 5)


account = BankAccount("Ali", 1000)
account.deposit(500)
account.show_balance()

shape = Shape()
square = Square()
circle = Circle()

shape.area()
square.area()
circle.area()
