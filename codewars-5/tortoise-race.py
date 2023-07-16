from math import floor


def race(v1, v2, g):
    if v1 >= v2:
        return None
    time = g * 3600 / (v2 - v1)
    return [floor(time / 3600), floor((time % 3600) / 60), floor(time % 60)]
