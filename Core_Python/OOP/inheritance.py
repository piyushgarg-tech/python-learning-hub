"""
Inheritance Quick Revision
"""

# Single Inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def intro(self):
        return f"I am {self.name}"


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


s = Student("Piyush", "Python")

print(s.intro())                 # Parent Method

print(s.course)                  # Child Variable


# Method Overriding

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


Dog().sound()


# Multilevel Inheritance

class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


c = C()

c.show()


# Multiple Inheritance

class Father:

    def skill1(self):
        print("Driving")


class Mother:

    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skill1()

child.skill2()


# MRO

print(Child.mro())