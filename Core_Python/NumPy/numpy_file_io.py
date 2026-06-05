"""
NumPy File Operations
"""

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Save

np.save("array.npy", arr)

# Load

loaded = np.load("array.npy")

print(loaded)

# Save Text

np.savetxt(
    "array.txt",
    arr,
    fmt="%d"
)

# Load Text

print(
    np.loadtxt(
        "array.txt",
        dtype=int
    )
)