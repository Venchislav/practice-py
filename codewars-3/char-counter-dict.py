def count(s):
    res = {}
    for elem in s:
        res[elem] = s.count(elem)
    return res


# Woah... Didn't really know that it's possible to use generator with dict!
def count(string):
    return {i: string.count(i) for i in string}
