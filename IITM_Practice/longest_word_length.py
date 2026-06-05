"""
Longest Word Problems
"""

sentence = """
Python is widely used in
Data Science Machine Learning
and Automation
"""


words = sentence.split()


# Longest Word

print(
    max(
        words,
        key=len
    )
)


# Length of Longest Word

print(
    len(
        max(
            words,
            key=len
        )
    )
)


# Shortest Word

print(
    min(
        words,
        key=len
    )
)


# Sort By Length

print(
    sorted(
        words,
        key=len
    )
)


# Top 3 Longest Words

print(
    sorted(
        words,
        key=len,
        reverse=True
    )[:3]
)


# Word Length Dictionary

word_lengths = {
    word: len(word)
    for word in words
}

print(word_lengths)


# Average Word Length

print(
    sum(
        map(len, words)
    ) / len(words)
)


# Most Frequent Word

text = """
python data python
science python data
"""

words = text.split()

freq = {}

for word in words:

    freq[word] = (
        freq.get(word, 0) + 1
    )

print(
    max(
        freq,
        key=freq.get
    )
)