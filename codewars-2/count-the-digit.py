def nb_dig(n, d):
    values_list = list(range(0, n+1))
    squared_lst = list(map(lambda x: str(x**2), values_list))
    str_lst = ''.join(squared_lst)
    return str_lst.count(str(d))

print(nb_dig(5750, 0))
