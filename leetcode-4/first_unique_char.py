def firstUniqChar(s):
    for i in sorted(set(s), key=s.index):
        if s.count(i) == 1:
            return s.index(i)
    return -1

print(firstUniqChar("aabb"))
