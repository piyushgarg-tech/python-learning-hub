"""
Common Python Mistakes
"""

# Mutable Default Argument

def add_item(item, items=[]):

    items.append(item)

    return items


print(add_item(1))

print(add_item(2))


# Correct Way

def add_item(item, items=None):

    if items is None:

        items = []

    items.append(item)

    return items


print(add_item(1))

print(add_item(2))


# Shallow Copy

a = [[1, 2]]

b = a.copy()

b[0][0] = 100

print(a)


# Deep Copy

from copy import deepcopy

a = [[1, 2]]

b = deepcopy(a)

b[0][0] = 100

print(a)


# List Multiplication Problem

matrix = [[0] * 3] * 3

matrix[0][0] = 1

print(matrix)


# Correct Matrix

matrix = [

    [0] * 3

    for _ in range(3)

]

matrix[0][0] = 1

print(matrix)


# Floating Point Precision

print(0.1 + 0.2)

print(round(0.1 + 0.2, 2))


# Dictionary KeyError

student = {
    "name": "Piyush"
}

print(
    student.get("age")
)


# Compare With None

x = None

print(x is None)

print(x is not None)