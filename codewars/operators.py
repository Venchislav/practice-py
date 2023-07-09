import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def basic_op(operator, value1, value2):
    return ops[operator](value1, value2)


print(basic_op('+', 4, 7))


# I wrote this code
# But code below is better in my opinion,
# So it's here

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))


print(basic_op('+', 4, 7))
