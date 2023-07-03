def g():
    print("I'm in func g")


def f():
    print("I'm in func f")
    g()
    print("I'm in func f")


print("I'm outside")
f()
print("I'm outside")
