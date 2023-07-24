def div_con(x):
    ints = [i for i in x if isinstance(i, int)]
    strs = [int(i) for i in x if isinstance(i, str)]
    return sum(ints) - sum(strs)
