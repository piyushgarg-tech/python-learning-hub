"""
Digit Operations
"""

n = 12345

# Sum of Digits

temp = n
digit_sum = 0

while temp:

    digit_sum += temp % 10

    temp //= 10

print(digit_sum)


# Count Digits

temp = n
count = 0

while temp:

    count += 1

    temp //= 10

print(count)


# Reverse Number

temp = n
reverse = 0

while temp:

    reverse = (
        reverse * 10 +
        temp % 10
    )

    temp //= 10

print(reverse)


# Largest Digit

temp = n
largest = 0

while temp:

    largest = max(
        largest,
        temp % 10
    )

    temp //= 10

print(largest)


# Armstrong Number

num = 153

power = len(str(num))

result = sum(
    int(digit) ** power
    for digit in str(num)
)

print(
    result == num
)