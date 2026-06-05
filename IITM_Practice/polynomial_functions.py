"""
Polynomial Functions
"""

# Evaluate Polynomial

def polynomial(coeffs, x):

    return sum(
        coeff * (x ** power)
        for power, coeff
        in enumerate(coeffs)
    )


coeffs = [-180, -144, 101, 52, -18, -4, 1]

print(
    polynomial(coeffs, 2)
)


# Find Integer Roots

def polynomial_roots(
    coeffs,
    start,
    end
):

    roots = []

    for x in range(
        start,
        end + 1
    ):

        if polynomial(coeffs, x) == 0:

            roots.append(x)

    return roots


print(
    polynomial_roots(
        coeffs,
        0,
        10
    )
)


# Derivative Coefficients

def derivative(coeffs):

    return [
        power * coeff
        for power, coeff
        in enumerate(coeffs)
        if power > 0
    ]


print(
    derivative(coeffs)
)


# Horner's Method

def horner(coeffs, x):

    result = 0

    for coeff in reversed(coeffs):

        result = result * x + coeff

    return result


print(
    horner(coeffs, 2)
)