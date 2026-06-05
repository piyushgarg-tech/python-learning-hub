"""
Loops Quick Revision
"""

# range()

print(list(range(5)))            # 0-4

print(list(range(1, 11)))        # 1-10

print(list(range(10, 0, -1)))    # Reverse

# For Loop

for i in range(5):
    print(i)

# While Loop

n = 5

while n:
    print(n)
    n -= 1

# Break

for i in range(10):
    if i == 5:
        break
    print(i)

# Continue

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Enumerate

names = ["Piyush", "Rahul", "Arun"]

for idx, name in enumerate(names, start=1):
    print(idx, name)

# Zip

a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a, b):
    print(x + y)

# Nested Loop

for i in range(3):
    for j in range(3):
        print(i, j)

# List Comprehension

squares = [x*x for x in range(10)]

print(squares)

# Conditional Comprehension

evens = [x for x in range(20) if x % 2 == 0]

print(evens)

# Generator Expression

print(sum(x*x for x in range(10)))

# Frequency Count

word = "programming"

freq = {}

for ch in word:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

# Reverse Iteration

for i in reversed(range(1, 6)):
    print(i)

# Loop Else

for i in range(5):
    print(i)
else:
    print("Completed")