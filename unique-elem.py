def stray(arr):
    for elem in arr:
        if arr.count(elem) == 1:
            return elem
