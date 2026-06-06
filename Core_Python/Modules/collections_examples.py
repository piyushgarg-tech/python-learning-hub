"""
Collections Module
"""

from collections import (
    Counter,
    defaultdict,
    deque
)


# Counter

word = "programming"

print(
    Counter(word)
)


# Most Common

print(
    Counter(word).most_common(3)
)


# defaultdict

data = defaultdict(list)

data["Python"].append("Piyush")

data["Python"].append("Rahul")

print(data)


# deque

queue = deque()

queue.append("A")

queue.append("B")

queue.append("C")

print(queue)

print(
    queue.popleft()
)

print(queue)


# Fixed Length deque

history = deque(
    maxlen=3
)

for i in range(1, 6):

    history.append(i)

print(history)