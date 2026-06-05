"""
Useful Python Utility Functions

Concepts Covered:
- max
- min
- sum
- len
- round
- abs
- Counter
- combinations
- divmod
- any
- all
- zip
"""

from collections import Counter
from itertools import combinations


nums = [10, 20, 30, 40, 50]

print(max(nums))
print(min(nums))
print(sum(nums))
print(len(nums))
print(round(3.14159, 2))
print(abs(-25))


# Counter

word = "programming"

print(Counter(word))


# Combinations

print(
    list(
        combinations(
            [1, 2, 3],
            2
        )
    )
)


# divmod

print(divmod(17, 5))


# any

print(any([0, 0, 1]))


# all

print(all([1, 1, 1]))


# zip

names = [
    "Piyush",
    "Rahul"
]

marks = [
    90,
    85
]

print(
    list(
        zip(
            names,
            marks
        )
    )
)