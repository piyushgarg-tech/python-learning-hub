"""
Password Generator

Concepts Covered:
- string module
- secrets module
- secure password generation
"""

import string
import secrets


length = 12

characters = (

    string.ascii_letters

    +

    string.digits

    +

    string.punctuation

)


password = "".join(

    secrets.choice(characters)

    for _ in range(length)

)

print(password)