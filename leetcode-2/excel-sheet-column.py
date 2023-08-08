def titleToNumber(column):
    res = 0
    for i in range(len(column)):
        res *= 26
        res += ord(column[i]) - ord('A') + 1

    return res
