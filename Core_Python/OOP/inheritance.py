"""
Inheritance Quick Revision
"""

# ==================================================
# 1. Single Inheritance
# ==================================================

print("\n--- Single Inheritance ---")


class Person:

    def __init__(self, name):
        self.name = name  # Parent attribute

    def intro(self):
        return f"I am {self.name}"  # Parent method


class Student(Person):  # Student inherits Person

    def __init__(self, name, course):
        super().__init__(name)  # Call parent constructor     """Can aslo use -(Person.__init__(self,name))""""
        self.course = course    # Child attribute

    def student_info(self):
        return f"{self.name} studies {self.course}"


s = Student("Piyush", "Python")

print(s.intro())         # Inherited method
print(s.student_info())  # Child method


# ==================================================
# 2. Method Overriding
# ==================================================

print("\n--- Method Overriding ---")


class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):  # Overrides parent method
        print("Dog barks")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# ==================================================
# 3. Multilevel Inheritance
# ==================================================

print("\n--- Multilevel Inheritance ---")


class Grandparent:

    def house(self):
        print("Grandparent's House")


class Parent(Grandparent):  # Parent inherits Grandparent

    def car(self):
        print("Parent's Car")


class Child(Parent):  # Child inherits Parent

    def bike(self):
        print("Child's Bike")


c = Child()

c.house()  # From Grandparent
c.car()    # From Parent
c.bike()   # Own method


# ==================================================
# 4. Multiple Inheritance
# ==================================================

print("\n--- Multiple Inheritance ---")


class Father:

    def driving(self):
        print("Can Drive")


class Mother:

    def cooking(self):
        print("Can Cook")


class Child(Father, Mother):  # Inherits from both classes
    pass


child = Child()

child.driving()  # From Father
child.cooking()  # From Mother


# ==================================================
# 5. Method Resolution Order (MRO)
# ==================================================

print("\n--- Method Resolution Order ---")


class A:

    def show(self):
        print("Class A")


class B(A):

    def show(self):
        print("Class B")


class C(A):

    def show(self):
        print("Class C")


class D(B, C):  # Multiple inheritance
    pass


d = D()

d.show()  # Python searches B before C

print("\nMRO:")
print(D.mro())  # Shows search order


# ==================================================
# 6. Useful Checks
# ==================================================

print("\n--- Useful Checks ---")

# Checks if object belongs to a class
print(isinstance(s, Student))

# Checks inheritance relationship
print(isinstance(s, Person))

# Checks class inheritance
print(issubclass(Student, Person))

print(issubclass(Dog, Animal))