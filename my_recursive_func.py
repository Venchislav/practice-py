def comb(n, k):
    if k == 0:
        return 1

    elif k > n:
        return 0

    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)


n, k = map(int, input().split())
print(comb(n, k))
