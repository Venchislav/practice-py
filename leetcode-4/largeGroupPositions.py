def largeGroupPositions(s):
    l = 0
    s += '0'
    res = []

    for idx, elem in enumerate(s):
        if elem != s[l]:
            if idx - l >= 3:
                res.append([l, idx-1])
            l = idx
    return res
print(largeGroupPositions("abcdddeeeeaabbbcd"))
