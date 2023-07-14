# Custom min-max funcs

def minimum(arr):
    min = float('inf')

    for itm in arr:
        if itm < min:
            min = itm
    return min


def maximum(arr):
    max = arr[0]

    for itm in arr:
        if itm > max:
            max = itm
    return max
