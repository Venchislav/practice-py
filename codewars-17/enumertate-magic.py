def _all(seq, fun):
    for i in seq:
        if not fun(i):
            return False
    return True
