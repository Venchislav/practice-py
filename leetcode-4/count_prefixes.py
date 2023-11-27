def countPrefixes(words, s):
    p = 0
    for w in words:
        if s.startswith(w):
            p += 1
    return p
