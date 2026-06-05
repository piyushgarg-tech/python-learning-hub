"""
Datetime Examples

Concepts Covered:
- datetime.now
- strftime
- strptime
- timedelta
- date difference
- weekday
"""

from datetime import (
    datetime,
    timedelta
)


# Current DateTime

now = datetime.now()

print(now)


# Formatting

print(
    now.strftime("%d-%m-%Y")
)

print(
    now.strftime("%H:%M:%S")
)


# String to Datetime

date_str = "06-06-2026"

date_obj = datetime.strptime(
    date_str,
    "%d-%m-%Y"
)

print(date_obj)


# Timedelta

future = now + timedelta(days=10)

past = now - timedelta(days=5)

print(future)

print(past)


# Date Difference

start = datetime(
    2026,
    1,
    1
)

end = datetime(
    2026,
    12,
    31
)

print(
    (end - start).days
)


# Weekday

print(
    now.weekday()
)

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print(
    days[now.weekday()]
)