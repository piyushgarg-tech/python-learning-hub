"""
Collections Quick Revision
"""

# ================= LIST =================

nums = [10, 20, 30, 40, 50]

print(nums[0])                   # First Element
print(nums[-1])                  # Last Element

print(nums[:3])                  # Slice
print(nums[::-1])                # Reverse

nums.append(60)                  # Add One
nums.extend([70, 80])            # Add Multiple

nums.insert(1, 15)               # Insert

nums.remove(30)                  # Remove

print(nums)

print(max(nums))                 # Maximum
print(min(nums))                 # Minimum
print(sum(nums))                 # Sum
print(len(nums))                 # Length

# List Comprehension

squares = [x**2 for x in range(1, 6)]

print(squares)

evens = [
    x for x in range(20)
    if x % 2 == 0
]

print(evens)

# ================= TUPLE =================

t = (10, 20, 30)

a, b, c = t                      # Unpacking

print(a, b, c)

print(t.count(10))
print(t.index(20))

# ================= SET =================

s = {1, 2, 3, 3, 4, 4}

print(s)                         # Unique Values

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)                     # Union
print(a & b)                     # Intersection
print(a - b)                     # Difference

# ================= DICTIONARY =================

student = {
    "name": "Piyush",
    "age": 20,
    "course": "Python"
}

print(student["name"])

print(student.get("age"))

student["city"] = "Hisar"

print(student.keys())            # Keys
print(student.values())          # Values
print(student.items())           # Key-Value Pairs

for k, v in student.items():
    print(k, v)

# Dictionary Comprehension

square_dict = {
    x: x**2
    for x in range(5)
}

print(square_dict)