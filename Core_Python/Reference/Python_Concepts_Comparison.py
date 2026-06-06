"""
Python Concepts Comparison
"""

# List vs Tuple

"""
List
-----
Mutable
[]
More Memory
More Methods

Tuple
------
Immutable
()
Less Memory
Faster
"""


# Set vs Dictionary

"""
Set
----
Unique Values
No Key-Value Pair

Dictionary
-----------
Key-Value Pair
Fast Lookup
"""


# sort() vs sorted()

nums = [3, 1, 2]

print(sorted(nums))      # New List

print(nums)

nums.sort()

print(nums)              # Original Changed


# append() vs extend()

a = [1, 2]

a.append([3, 4])

print(a)

b = [1, 2]

b.extend([3, 4])

print(b)


# remove() vs pop()

nums = [10, 20, 30]

nums.remove(20)

print(nums)

nums.pop()

print(nums)


# == vs is

a = [1, 2]

b = [1, 2]

print(a == b)

print(a is b)


# Shallow vs Deep Copy

from copy import copy, deepcopy

a = [[1, 2]]

b = copy(a)

c = deepcopy(a)

print(b)

print(c)


# / vs //

print(5 / 2)

print(5 // 2)


# Mutable vs Immutable

"""
Mutable
--------
list
set
dict

Immutable
----------
tuple
str
int
float
"""


# map() vs filter()

nums = [1, 2, 3, 4]

print(
    list(
        map(
            lambda x: x**2,
            nums
        )
    )
)

print(
    list(
        filter(
            lambda x: x % 2 == 0,
            nums
        )
    )
)


# Class Variable vs Instance Variable

class Student:

    school = "IITM"          # Class Variable

    def __init__(self, name):
        self.name = name     # Instance Variable


s = Student("Piyush")

print(Student.school)

print(s.name)