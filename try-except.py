def foo(): return 5 / 0


try:
    foo()
except (ArithmeticError, AssertionError, ZeroDivisionError) as e:
    print(e)
