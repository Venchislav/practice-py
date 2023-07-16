def find_it(seq):
    return [i for i in seq if seq.count(i) % 2 != 0][0]
