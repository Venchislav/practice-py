def areOccurrencesEqual(s):
    counts = []
    for c in set(s):
        counts.append(s.count(c))
    return len(set(counts)) == 1


print(areOccurrencesEqual("aaabb"))
