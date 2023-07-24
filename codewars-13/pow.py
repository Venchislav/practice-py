def number_to_pwr(n, p):
    d=1
    for i in range(1, p+1):
        d=d*n
    return d


print(number_to_pwr(4, 2))
