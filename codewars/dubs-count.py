from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())

    total = 0
    for char in counter:
        if counter[char] > 1:
            total += 1
    return total
