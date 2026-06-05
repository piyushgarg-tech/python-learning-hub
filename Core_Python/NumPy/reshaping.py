"""
NumPy Reshaping
"""

import numpy as np

arr = np.arange(12)

print(arr)

matrix = arr.reshape(3,4)

print(matrix)               # 3x4

print(matrix.T)             # Transpose

print(matrix.ravel())       # Flatten

print(matrix.reshape(2,6))  # New Shape