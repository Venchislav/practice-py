def hammingWeight(n):
    counter = collections.Counter(bin(n)[2:])
    return counter.get("1", 0)
