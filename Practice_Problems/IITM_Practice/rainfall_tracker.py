"""
Rainfall Tracker
"""

rainfall = {
    "Jan": 25,
    "Feb": 40,
    "Mar": 18,
    "Apr": 65,
    "May": 55,
    "Jun": 80
}


# Total Rainfall

print(
    sum(
        rainfall.values()
    )
)


# Average Rainfall

print(
    sum(
        rainfall.values()
    ) / len(rainfall)
)


# Highest Rainfall Month

print(
    max(
        rainfall,
        key=rainfall.get
    )
)


# Lowest Rainfall Month

print(
    min(
        rainfall,
        key=rainfall.get
    )
)


# Above Average Months

avg = (
    sum(rainfall.values())
    / len(rainfall)
)

print(
    [
        month
        for month, value
        in rainfall.items()
        if value > avg
    ]
)


# Sorted Report

print(
    sorted(
        rainfall.items(),
        key=lambda x: x[1],
        reverse=True
    )
)


# Rainfall Category

for month, value in rainfall.items():

    if value >= 70:

        status = "Heavy"

    elif value >= 40:

        status = "Moderate"

    else:

        status = "Low"

    print(
        month,
        status
    )