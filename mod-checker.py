def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_3 = mod_checker(3)
print(mod_3(3))  # True
print(mod_3(4))  # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))  # True

mod_checker = lambda x, mod=0: lambda y: y % x == mod

a = [1, 2, 3, 4, 5, 6, 7]
lower, upper = 0, 5

var = a[lower:: upper]
var = a[lower:upper], a[lower:upper:], a[lower::step]
var = a[lower+offset : upper+offset]
var = a[lower + offset : upper + offset]
var = a[lower + offset:upper + offset]
