"""
Input / Output Quick Revision
"""

# Basic Input

name = input("Name: ")
print(name)

# Integer Input

n = int(input())
print(n)

# Float Input

salary = float(input())
print(salary)

# Multiple Inputs

a, b = map(int, input().split())

print(a + b)

# List Input

nums = list(map(int, input().split()))

print(nums)

# Matrix Input

matrix = [
    list(map(int, input().split()))
    for _ in range(3)
]

print(matrix)

# String Formatting

name = "Piyush"
age = 20

print(f"{name} is {age}")        # f-string

print(
    "{} is {}".format(name, age)
)                                # format()

# Unpacking

x, y, z = [10, 20, 30]

print(x, y, z)

# Enumerate

fruits = ["Apple", "Banana", "Mango"]

for idx, fruit in enumerate(fruits, start=1):
    print(idx, fruit)            # Index + Value

# Zip

names = ["Piyush", "Rahul"]
marks = [90, 85]

for name, mark in zip(names, marks):
    print(name, mark)

# Date Parsing

dob = "06/06/2005"

day, month, year = map(int, dob.split("/"))

print(day, month, year)