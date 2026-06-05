"""
Advanced OOP Quick Revision
"""

from abc import ABC, abstractmethod


# Encapsulation

class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = Account(1000)

acc.deposit(500)

print(acc.get_balance())          # 1500


# Property Decorator

class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value


e = Employee(50000)

e.salary = 60000

print(e.salary)


# Polymorphism

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:

    animal.sound()


# Abstraction

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


sq = Square(5)

print(sq.area())


# Operator Overloading

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)

n2 = Number(20)

print(n1 + n2)


# Duck Typing

class Student:

    def intro(self):
        print("Student")


class Teacher:

    def intro(self):
        print("Teacher")


for person in [Student(), Teacher()]:

    person.intro()