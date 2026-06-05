"""
Prime Number Problems
"""

# Prime Check

def is_prime(n):

    if n < 2:
        return False

    for i in range(
        2,
        int(n ** 0.5) + 1
    ):

        if n % i == 0:
            return False

    return True


print(
    is_prime(97)
)


# Prime Numbers in Range

primes = [

    num

    for num in range(2, 101)

    if is_prime(num)

]

print(primes)


# Count Primes

print(
    len(primes)
)


# Prime Factors

num = 84

factors = []

factor = 2

while factor * factor <= num:

    while num % factor == 0:

        factors.append(factor)

        num //= factor

    factor += 1

if num > 1:

    factors.append(num)

print(factors)


# Sieve of Eratosthenes

n = 100

sieve = [True] * (n + 1)

sieve[0] = sieve[1] = False

for i in range(
    2,
    int(n ** 0.5) + 1
):

    if sieve[i]:

        for j in range(
            i * i,
            n + 1,
            i
        ):

            sieve[j] = False

print(

    [
        i
        for i in range(n + 1)
        if sieve[i]
    ]

)


# Twin Primes

for i in range(
    len(primes) - 1
):

    if primes[i + 1] - primes[i] == 2:

        print(
            (primes[i], primes[i + 1])
        )