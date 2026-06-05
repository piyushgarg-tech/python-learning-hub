"""
Searching Algorithms
"""

# Linear Search

def linear_search(nums, target):

    for i, value in enumerate(nums):

        if value == target:
            return i

    return -1


nums = [10, 20, 30, 40, 50]

print(
    linear_search(nums, 30)
)                               # Index


# Binary Search

def binary_search(nums, target):

    left = 0

    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


nums = [10, 20, 30, 40, 50]

print(
    binary_search(nums, 40)
)


# Membership Search

nums = [5, 10, 15, 20]

print(15 in nums)               # True

print(100 in nums)              # False