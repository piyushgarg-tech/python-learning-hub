"""
OOP Basics Quick Revision
"""

# Class & Object

class Student:

    school = "IITM"                  # Class Variable
    total_students = 0

    def __init__(self, name, age, marks):
        self.name = name             # Instance Variable
        self.age = age
        self.marks = marks

        Student.total_students += 1

    def display(self):
        return (
            f"{self.name} | "
            f"{self.age} | "
            f"{self.marks}"
        )

    def is_pass(self):
        return self.marks >= 40

    @classmethod
    def total(cls):
        return cls.total_students

    @staticmethod
    def info():
        return "Student Class"


# Objects

s1 = Student("Piyush", 20, 85)

s2 = Student("Rahul", 21, 35)

print(s1.display())              # Object Method

print(s2.display())

print(s1.is_pass())              # True

print(s2.is_pass())              # False

print(Student.total())           # Total Objects

print(Student.info())            # Static Method


# Magic Method

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book({self.pages} pages)"


print(Book(200))