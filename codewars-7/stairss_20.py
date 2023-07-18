def stairs_in_20(stairs):
    total = 0
    for i in stairs: total += sum(i)
    return total * 20


# shorter solution

def stairs_in_20(stairs):
    return sum(sum(x) for x in stairs) * 20
