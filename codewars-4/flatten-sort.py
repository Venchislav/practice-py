def flatten_and_sort(array):
    res = []
    for i in array:
        for j in i:
            res.append(j)
    return sorted(res)


# shorter version

def flatten_and_sort(array):
    return sorted([j for i in array for j in i])
