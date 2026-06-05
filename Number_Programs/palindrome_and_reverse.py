"""
Palindrome & Reverse Problems
"""

# Reverse String (Slicing)

text = "python"

print(
    text[::-1]
)


# Reverse String (Manual)

text = "python"

reverse = ""

for ch in text:

    reverse = ch + reverse

print(reverse)


# String Palindrome

word = "madam"

print(
    word == word[::-1]
)


# Two Pointer Palindrome

word = "racecar"

left = 0

right = len(word) - 1

is_palindrome = True

while left < right:

    if word[left] != word[right]:

        is_palindrome = False

        break

    left += 1

    right -= 1

print(is_palindrome)


# Reverse Number

num = 12345

temp = num

reverse = 0

while temp:

    reverse = (
        reverse * 10 +
        temp % 10
    )

    temp //= 10

print(reverse)


# Number Palindrome

num = 12321

temp = num

reverse = 0

while temp:

    reverse = (
        reverse * 10 +
        temp % 10
    )

    temp //= 10

print(
    num == reverse
)


# Palindrome List

words = [
    "madam",
    "python",
    "level",
    "data"
]

print(
    [
        word
        for word in words
        if word == word[::-1]
    ]
)