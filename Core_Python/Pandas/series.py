"""
Pandas Series
"""

import pandas as pd

s = pd.Series([10,20,30,40])

print(s)

print(s.values)             # Values

print(s.index)              # Index

print(s.mean())             # Mean

print(s.max())              # Max

print(s.min())              # Min

print(s.describe())         # Statistics