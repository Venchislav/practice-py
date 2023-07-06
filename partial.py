from functools import partial

int_2 = partial(int, base=2)
print(int_2("1101"))
print(int_2("11010110"))
