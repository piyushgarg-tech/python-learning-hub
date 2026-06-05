"""
NumPy Indexing & Slicing
"""

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr[0])               # First Row

print(arr[:,1])             # Second Column

print(arr[1,2])             # Element

print(arr[:2,:2])           # Sub Matrix

print(arr[::-1])            # Reverse Rows

print(arr.flatten())        # 1D Array