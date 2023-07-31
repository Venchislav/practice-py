from collections import Counter
def ordered_count(input):
    c = Counter(input)
    return sorted(list(c.items()), key=lambda x: input.index(x[0]))
