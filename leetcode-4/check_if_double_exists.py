def checkIfExist(arr):
    # if we have 2 0s we can multiply 0 * 2 and get 0, which is in arr
    if arr.count(0) > 1: return True
    # remove 0s if it contains only one 0.
    s = set(arr) - {0}
    for a in arr:
        if a * 2 in s:
            return True
    return False


print(checkIfExist([10,2,5,3]))
print(checkIfExist([-2,0,10,-19,4,6,-8]))
