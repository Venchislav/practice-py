def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x - (x % 5) + 5


print(closest_mod_5(47))
