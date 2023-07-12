import operator

ops = {"add": operator.add, "subtract": operator.sub, "multiply": operator.mul, "divide": operator.truediv}


def arithmetic(a, b, operator):
    return ops[operator](a, b)
