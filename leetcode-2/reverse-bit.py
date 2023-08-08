def reverseBits(n):
    a = bin(n)
    a = a[2:]
    a = a[::-1] + ("0" * (32 - len(a)))
    return int(a, 2)
