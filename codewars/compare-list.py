from collections import Counter

comp = lambda a, b: a is not None and b is not None and Counter(map(lambda x: x * x, a)) == Counter(b)
