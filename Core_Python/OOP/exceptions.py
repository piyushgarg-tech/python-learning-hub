"""
Exception Handling Quick Revision
"""

# ==================================================
# 1. Basic Exception Handling
# ==================================================

print("\n--- Basic Exception ---")

try:
    print(10 / 0)  # Error occurs here

except ZeroDivisionError:
    print("Cannot divide by zero")


# ==================================================
# 2. Multiple Exceptions
# ==================================================

print("\n--- Multiple Exceptions ---")

try:
    nums = [1, 2, 3]

    print(nums[10])  # Invalid index

except IndexError:
    print("Index out of range")

except Exception as e:
    # Generic exception (keep last)
    print(e)


# ==================================================
# 3. Else Block
# ==================================================

print("\n--- Else Block ---")

try:
    num = 10

    print(num)

except Exception:
    print("Something went wrong")

else:
    # Runs only if no exception occurs
    print("No Exception Found")


# ==================================================
# 4. Finally Block
# ==================================================

print("\n--- Finally Block ---")

try:
    print("Opening File")

finally:
    # Always executes
    print("Closing File")


# ==================================================
# 5. Raising Exceptions
# ==================================================

print("\n--- Raise Exception ---")


def withdraw(balance, amount):

    if amount > balance:

        raise ValueError(
            "Insufficient Balance"
        )

    return balance - amount


print(withdraw(5000, 1000))


# ==================================================
# 6. Custom Exception
# ==================================================

print("\n--- Custom Exception ---")


class InvalidMarksError(Exception):
    # Custom exception inherits Exception
    pass


def validate_marks(marks):

    if not 0 <= marks <= 100:

        raise InvalidMarksError(
            "Marks must be between 0 and 100"
        )


validate_marks(90)

print("Marks Valid")


# ==================================================
# 7. Practical Validation
# ==================================================

print("\n--- Validation Example ---")


def validate_age(age):

    if age < 0:

        raise ValueError(
            "Age cannot be negative"
        )

    return age


print(validate_age(20))


# ==================================================
# 8. Catching Exception Object
# ==================================================

print("\n--- Exception Object ---")

try:

    number = int("abc")

except ValueError as e:

    print("Error:", e)


# ==================================================
# 9. Quick Revision Notes
# ==================================================

# try
# Code that may raise an exception

# except
# Handles specific exceptions

# else
# Runs if no exception occurs

# finally
# Runs whether exception occurs or not

# raise
# Manually create an exception

# Custom Exception
# User-defined exception class

# Exception as e
# Access actual error message