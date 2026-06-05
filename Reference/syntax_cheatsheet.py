"""
Syntax Cheatsheet
"""

# List Comprehension

squares = [
    x**2
    for x in range(10)
]


# Conditional Comprehension

evens = [
    x
    for x in range(20)
    if x % 2 == 0
]


# Dictionary Comprehension

square_dict = {
    x: x**2
    for x in range(5)
}


# Set Comprehension

unique = {
    x % 3
    for x in range(10)
}


# Lambda

square = lambda x: x**2


# map()

nums = [1, 2, 3]

result = list(
    map(
        lambda x: x**2,
        nums
    )
)


# filter()

result = list(
    filter(
        lambda x: x % 2 == 0,
        nums
    )
)


# sorted()

students = [
    ("A", 90),
    ("B", 80),
    ("C", 95)
]

sorted_students = sorted(
    students,
    key=lambda x: x[1],
    reverse=True
)


# enumerate()

for idx, value in enumerate(nums):
    pass


# zip()

for a, b in zip(
    [1,2,3],
    [4,5,6]
):
    pass


# Exception Handling

try:
    x = 10 / 0

except ZeroDivisionError:
    pass


# File Handling

with open("file.txt") as f:

    data = f.read()


# Class Skeleton

class Student:

    def __init__(
        self,
        name
    ):
        self.name = name

    def display(self):
        return self.name


# NumPy

import numpy as np

arr = np.array([1,2,3])

arr.reshape(3,1)


# Pandas

import pandas as pd

df = pd.read_csv(
    "data.csv"
)

df.head()

df.describe()

df.groupby(
    "column"
).size()