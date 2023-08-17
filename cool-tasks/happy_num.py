def isHappy(self, n):
    processed = set()
    while n not in processed:
        processed.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

    return n == 1
