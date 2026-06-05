"""
Trader Profit Loss Analysis
"""

prices = [
    100, 120, 90,
    150, 110, 180
]


# Daily Profit / Loss

changes = [

    prices[i] - prices[i - 1]

    for i in range(1, len(prices))
]

print(changes)


# Total Profit

print(
    sum(
        x for x in changes
        if x > 0
    )
)


# Total Loss

print(
    abs(
        sum(
            x for x in changes
            if x < 0
        )
    )
)


# Best Profit Day

print(
    max(changes)
)


# Worst Loss Day

print(
    min(changes)
)


# Buy Low Sell High

buy_price = min(prices)

sell_price = max(
    prices[
        prices.index(buy_price):
    ]
)

print(
    sell_price - buy_price
)


# Running Profit

profit = 0

for change in changes:

    profit += change

    print(profit)