"""
Advanced OOP Quick Revision
"""

from abc import ABC, abstractmethod


# ==================================================
# 1. Encapsulation
# ==================================================

print("\n--- Encapsulation ---")


class Account:

    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Controlled access


acc = Account(1000)

acc.deposit(500)

print(acc.get_balance())  # 1500

# print(acc.__balance)  # Error


# ==================================================
# 2. Property Decorator
# ==================================================

print("\n--- Property Decorator ---")


class Employee:

    def __init__(self, salary):
        self._salary = salary  # Protected variable

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value > 0:
            self._salary = value


e = Employee(50000)

e.salary = 60000  # Calls setter automatically

print(e.salary)   # Calls getter automatically


# ==================================================
# 3. Polymorphism
# ==================================================

print("\n--- Polymorphism ---")


class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:

    animal.sound()  # Same method, different behavior


# ==================================================
# 4. Abstraction
# ==================================================

print("\n--- Abstraction ---")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # Must be implemented


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


sq = Square(5)

print(sq.area())

# Shape()  # Error: abstract class


# ==================================================
# 5. Operator Overloading
# ==================================================

print("\n--- Operator Overloading ---")


class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)

n2 = Number(20)

print(n1 + n2)  # Calls __add__()


# ==================================================
# 6. Duck Typing
# ==================================================

print("\n--- Duck Typing ---")


class Student:

    def intro(self):
        print("Student")


class Teacher:

    def intro(self):
        print("Teacher")


for person in [Student(), Teacher()]:

    person.intro()

# Python only cares that intro() exists


# ==================================================
# 7. Name Mangling
# ==================================================

print("\n--- Name Mangling ---")

print(acc._Account__balance)

# Python internally converts:
# __balance
# to
# _Account__balance


# ==================================================
# 8. Quick Revision Notes
# ==================================================

# Encapsulation
# Hides data using private variables

# Property
# Getter/Setter without explicit methods

# Polymorphism
# Same interface, different behavior

# Abstraction
# Defines what must be implemented

# Operator Overloading
# Customize operators (+, -, *, etc.)

# Duck Typing
# If object has required method, it works