def reverse_seq(n):
    return [i + 1 for i in range(n)][::-1]


# But better use

def reverse_seq(n):
    return list(range(n, 0, -1))
