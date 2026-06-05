"""
Functions Quick Revision
"""

# Basic Function

def greet(name):
    return f"Hello {name}"

print(greet("Piyush"))

# Default Argument

def welcome(name="Guest"):
    return f"Welcome {name}"

print(welcome())

# Multiple Arguments

def add(a, b):
    return a + b

print(add(10, 20))

# *args

def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4, 5))

# **kwargs

def student(**data):
    return data

print(student(name="Piyush", age=20))

# Higher Order Function

def apply(func, value):
    return func(value)

print(apply(abs, -10))

# Practical Example

def c_to_f(c):
    return (9/5) * c + 32

print(c_to_f(37))