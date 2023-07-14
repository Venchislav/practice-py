def solve(s):
    up = 0
    lw = 0

    for elem in s:
        if elem.isupper():
            up += 1
        else:
            lw += 1

    return s.upper() if up > lw else s.lower()

