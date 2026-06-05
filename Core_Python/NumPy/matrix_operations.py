"""
NumPy Matrix Operations
"""

import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A + B)                # Addition

print(A - B)                # Subtraction

print(A * B)                # Element Wise

print(A @ B)                # Matrix Multiplication

print(np.dot(A,B))          # Dot Product

print(np.linalg.det(A))     # Determinant

print(np.linalg.inv(A))     # Inverse