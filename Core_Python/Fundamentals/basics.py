"""
Python Fundamentals Quick Revision
"""

# Multiple Assignment

a, b, c = 10, 20, 30
print(a, b, c)                    # Unpacking

# Data Types

name = "Piyush"
age = 20
salary = 15000.50
is_student = True

print(type(name))                 # str
print(type(age))                  # int
print(type(salary))               # float
print(type(is_student))           # bool

# Arithmetic Operators

x, y = 10, 3

print(x + y)                      # Addition
print(x - y)                      # Subtraction
print(x * y)                      # Multiplication
print(x / y)                      # Division
print(x // y)                     # Floor Division
print(x % y)                      # Modulus
print(x ** y)                     # Power

# Relational Operators

print(x > y)                      # Greater Than
print(x == y)                     # Equal
print(x != y)                     # Not Equal

# Logical Operators

print(True and False)             # AND
print(True or False)              # OR
print(not True)                   # NOT

# Chained Comparison

print(10 < 20 < 30)              # True

# Type Conversion

print(int("10"))                 # str -> int
print(float("10"))               # str -> float
print(str(10))                   # int -> str

# Truthy & Falsy

values = [0, 1, "", "hello", [], [1], None]

for v in values:
    print(v, bool(v))            # Boolean Value

# Variable Swap

a, b = 5, 10
a, b = b, a

print(a, b)                      # Swapped

# Useful Built-ins

print(abs(-10))                  # Absolute Value
print(round(3.14159, 2))         # Rounding
print(pow(2, 5))                 # Power
print(max(10, 20, 30))           # Maximum
print(min(10, 20, 30))           # Minimum

# Ternary Operator

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)