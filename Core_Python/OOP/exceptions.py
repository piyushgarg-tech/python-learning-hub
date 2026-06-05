"""
Exception Handling
"""

# Basic Exception

try:

    print(10 / 0)

except ZeroDivisionError:

    print("Cannot divide by zero")


# Multiple Exceptions

try:

    nums = [1, 2, 3]

    print(nums[10])

except IndexError:

    print("Invalid Index")

except Exception as e:

    print(e)


# Else Block

try:

    num = 10

    print(num)

except Exception:

    print("Error")

else:

    print("No Exception")


# Finally Block

try:

    print("Opening File")

finally:

    print("Closing File")


# Raise Exception

def withdraw(balance, amount):

    if amount > balance:

        raise ValueError(
            "Insufficient Balance"
        )

    return balance - amount


print(
    withdraw(5000, 1000)
)


# Custom Exception

class InvalidMarksError(Exception):

    pass


def validate_marks(marks):

    if not 0 <= marks <= 100:

        raise InvalidMarksError(
            "Marks must be between 0 and 100"
        )


validate_marks(90)


# Practical Validation

def validate_age(age):

    if age < 0:

        raise ValueError(
            "Age cannot be negative"
        )

    return age


print(
    validate_age(20)
)