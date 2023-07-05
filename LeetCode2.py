def strStr(haystack, needle, index=0):
    n, h = len(needle), len(haystack)
    # hash_n = hash(needle)
    for i in range(h - n + 1):
        if haystack[i:i + n] == needle:
            return i
    return -1


print(strStr('addfhjks', 'sad'))
