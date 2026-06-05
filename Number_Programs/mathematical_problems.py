"""
Mathematical Problems
"""

# GCD

def gcd(a, b):

    while b:

        a, b = b, a % b

    return a


print(
    gcd(48, 18)
)


# LCM

def lcm(a, b):

    return (
        a * b
    ) // gcd(a, b)


print(
    lcm(12, 18)
)


# Fibonacci

a, b = 0, 1

for _ in range(10):

    print(a, end=" ")

    a, b = b, a + b

print()


# Armstrong

num = 153

power = len(str(num))

result = sum(
    int(digit) ** power
    for digit in str(num)
)

print(result == num)


# Perfect Number

num = 28

factors = [

    i

    for i in range(1, num)

    if num % i == 0

]

print(
    sum(factors) == num
)


# Prime Factorization

num = 84

factor = 2

factors = []

while factor * factor <= num:

    while num % factor == 0:

        factors.append(factor)

        num //= factor

    factor += 1

if num > 1:

    factors.append(num)

print(factors)


# Fast Power

def power(a, b):

    result = 1

    while b:

        if b % 2:

            result *= a

        a *= a

        b //= 2

    return result


print(
    power(2, 10)
)