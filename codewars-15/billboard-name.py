def billboard(name, price=30):
    x = price
    for i in range(len(name)):
        price += x
    return price - x


def billboard(name, price=30):
    return sum(price for letter in name)
