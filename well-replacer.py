"""
import sys

sys.setrecursionlimit(10 ** 6)

d1: int = 0


def recurs(s, a, b, d=d1):
    global d1
    if d >= 1000:
        return 'impossible'

    elif b not in s:
        return 0

    else:
        if s.count(b) != len(s):
            d1 += 1
            return recurs(s.replace(a, b), a, b, d=d1)
        else:
            return d


s = input()
a = input()

b = input()


print(recurs(s, a, b))
"""


def foo(s, a, b, d=0):
    if a in b and a in s:
        return 'Impossible'
    if s == s.replace(a, b):
        return d
    else:
        d += 1
        s = s.replace(a, b)
        return foo(s, a, b, d)
