"""
Sorting Algorithms
"""

nums = [5, 2, 8, 1, 9]

# Built-in Sort

print(sorted(nums))

print(sorted(nums, reverse=True))


# Bubble Sort

arr = nums.copy()

for i in range(len(arr)):

    for j in range(
        len(arr) - i - 1
    ):

        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = (
                arr[j + 1],
                arr[j]
            )

print(arr)


# Sort by Length

words = [
    "python",
    "java",
    "c"
]

print(
    sorted(
        words,
        key=len
    )
)