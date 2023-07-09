data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]


def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data]


print(open_or_senior(data))
