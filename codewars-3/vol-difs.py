import numpy as np


def find_difference(a, b):
    return max(np.prod(a), np.prod(b)) - min(np.prod(a), np.prod(b))


# close to the best

def find_difference(a, b):
    return abs(prod(a) - prod(b))
