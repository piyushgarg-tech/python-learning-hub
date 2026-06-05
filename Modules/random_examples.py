"""
Random Module Quick Revision
"""

import random

print(random.random())            # 0-1 Float

print(random.randint(1, 10))      # Inclusive

print(random.randrange(1, 20, 2)) # Step

nums = list(range(10))

print(random.choice(nums))        # One Item

print(random.sample(nums, 3))     # Multiple Items

random.shuffle(nums)              # In Place

print(nums)