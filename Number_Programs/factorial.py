"""
Factorial Applications
"""

from math import factorial


# Iterative

def factorial_iter(n):

    result = 1

    for i in range(
        2,
        n + 1
    ):

        result *= i

    return result


print(
    factorial_iter(5)
)


# Recursive

def factorial_rec(n):

    if n <= 1:

        return 1

    return (
        n *
        factorial_rec(n - 1)
    )


print(
    factorial_rec(5)
)


# Built-in

print(
    factorial(5)
)


# Permutation nPr

def npr(n, r):

    return (

        factorial(n)

        //

        factorial(n - r)

    )


print(
    npr(5, 2)
)


# Combination nCr

def ncr(n, r):

    return (

        factorial(n)

        //

        (
            factorial(r)

            *

            factorial(n - r)

        )

    )


print(
    ncr(5, 2)
)


# Pascal Triangle

n = 5

for i in range(n):

    row = [

        ncr(i, j)

        for j in range(i + 1)

    ]

    print(row)