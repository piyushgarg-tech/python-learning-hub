"""
Python Tricks - IITM & Real Usage
"""

from collections import Counter

# Swap

a, b = 10, 20

a, b = b, a

print(a, b)


# Frequency Counter

word = "programming"

print(Counter(word))


# Matrix Transpose

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(
    list(zip(*matrix))
)


# Flatten Matrix

flat = [
    item
    for row in matrix
    for item in row
]

print(flat)


# Dictionary Sort

marks = {
    "Rahul": 90,
    "Piyush": 95,
    "Arun": 85
}

print(
    sorted(
        marks.items(),
        key=lambda x: x[1],
        reverse=True
    )
)


# Remove Duplicates Preserve Order

nums = [1,2,2,3,1,4]

print(
    list(dict.fromkeys(nums))
)


# Group Data

names = ["A", "B", "C"]

scores = [90, 80, 95]

print(
    dict(zip(names, scores))
)


# Max by Key

students = [
    {"name":"A","marks":80},
    {"name":"B","marks":95},
    {"name":"C","marks":88}
]

print(
    max(
        students,
        key=lambda x: x["marks"]
    )
)


# Multiple Integer Input

nums = list(
    map(
        int,
        "10 20 30".split()
    )
)

print(nums)


# Nested List Creation

matrix = [
    [0] * 3
    for _ in range(3)
]

print(matrix)


# Any / All

print(any([0, 0, 1]))

print(all([1, 1, 1]))