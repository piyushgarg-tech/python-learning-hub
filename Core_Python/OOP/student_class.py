"""
OOP Basics Quick Revision
"""

# ==================================================
# 1. Class & Object
# ==================================================

class Student:

    school = "IITM"          # Class variable (shared by all objects)
    total_students = 0       # Tracks total objects created

    def __init__(self, name, age, marks):
        self.name = name     # Instance variable (unique per object)
        self.age = age
        self.marks = marks

        Student.total_students += 1  # Increase count on object creation

    def display(self):
        return (
            f"{self.name} | "
            f"{self.age} | "
            f"{self.marks}"
        )

    def is_pass(self):
        return self.marks >= 40  # Instance method using object data

    @classmethod
    def total(cls):
        return cls.total_students  # Works with class variables

    @staticmethod
    def info():
        return "Student Class"  # Independent utility method


# Creating Objects

s1 = Student("Piyush", 20, 85)

s2 = Student("Rahul", 21, 35)

print(s1.display())       # Object 1 details

print(s2.display())       # Object 2 details

print(s1.is_pass())       # True

print(s2.is_pass())       # False

print(Student.total())    # Total objects created

print(Student.info())     # Static method call


# ==================================================
# 2. Magic Method (__str__)
# ==================================================

class Book:

    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        # Defines how object appears when printed
        return f"Book({self.pages} pages)"


book = Book(200)

print(book)               # Calls __str__ automatically


# ==================================================
# 3. Quick Revision Notes
# ==================================================

# Class Variable
# Shared by all objects
print(Student.school)

# Instance Variable
# Different for each object
print(s1.name)

# Class Method
# Accesses class-level data
print(Student.total())

# Static Method
# Utility function related to class
print(Student.info())

# Magic Method
# Special built-in method
print(book)