"""
Lambda / Map / Filter Quick Revision
"""

# Lambda

square = lambda x: x**2

print(square(5))

# Map

nums = [1, 2, 3, 4, 5]

print(
    list(
        map(lambda x: x**2, nums)
    )
)

# Filter

print(
    list(
        filter(lambda x: x % 2 == 0, nums)
    )
)

# Sorted with Lambda

students = [
    ("Piyush", 80),
    ("Rahul", 95),
    ("Arun", 75)
]

print(
    sorted(
        students,
        key=lambda x: x[1]
    )
)

# Reduce

from functools import reduce

print(
    reduce(
        lambda a, b: a + b,
        nums
    )
)

# IITM Style One-Liner

result = sum(
    map(
        lambda x: x**2,
        filter(
            lambda x: x % 2 == 0,
            nums
        )
    )
)

print(result)