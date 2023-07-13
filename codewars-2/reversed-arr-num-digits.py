def digitize(n):
    return [int(i) for i in list(str(n))[::-1]]


# But better

def digitize(n):
    return list(map(int, str(n)[::-1]))


print(digitize(12354))
