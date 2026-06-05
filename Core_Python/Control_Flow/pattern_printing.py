"""
Pattern Printing Quick Revision
"""

n = 5

# Right Triangle

for i in range(1, n + 1):
    print("*" * i)

# Inverted Triangle

for i in range(n, 0, -1):
    print("*" * i)

# Pyramid

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Hollow Square

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")