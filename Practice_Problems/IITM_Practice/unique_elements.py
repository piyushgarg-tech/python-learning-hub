"""
Unique Elements
"""

nums = [
    10, 20, 10, 30,
    40, 20, 50, 30
]


# Method 1 : Set

print(
    list(set(nums))
)


# Method 2 : Preserve Order

seen = set()

unique = []

for num in nums:

    if num not in seen:

        seen.add(num)

        unique.append(num)

print(unique)


# Method 3 : Frequency Count

freq = {}

for num in nums:

    freq[num] = (
        freq.get(num, 0) + 1
    )

print(freq)


# Truly Unique Elements

print(
    [
        num
        for num, count
        in freq.items()
        if count == 1
    ]
)


# Duplicate Elements

print(
    [
        num
        for num, count
        in freq.items()
        if count > 1
    ]
)


# Intersection

a = [1, 2, 3, 4]

b = [3, 4, 5, 6]

print(
    list(
        set(a) & set(b)
    )
)


# Union

print(
    list(
        set(a) | set(b)
    )
)


# Difference

print(
    list(
        set(a) - set(b)
    )
)