"""
itertools Module
"""

from itertools import (
    permutations,
    combinations,
    product
)

# Permutations

print(
    list(
        permutations(
            [1, 2, 3],
            2
        )
    )
)

# Combinations

print(
    list(
        combinations(
            [1, 2, 3],
            2
        )
    )
)

# Cartesian Product

print(
    list(
        product(
            [1, 2],
            ["A", "B"]
        )
    )
)