"""
Advanced NumPy
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Boolean Indexing
print(arr[arr > 25])

# np.where
print(np.where(arr > 25, "High", "Low"))

# Broadcasting
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix + 10)

# Random Arrays
print(np.random.randint(1, 100, size=(3, 3)))

# Statistics
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))