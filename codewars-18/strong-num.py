import math


def strong_num(n):
    res = 0
    for i in str(n):
        res += math.factorial(int(i))
    return "STRONG!!!!" if str(res) == str(n) else "Not Strong !!"


# shorter solution
def strong_num(n):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(n)) == n else "Not Strong !!"
