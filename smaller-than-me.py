def smaller(arr):
    res = []
    for i in range(len(arr)):
        slice = arr[i:]
        c_res = [j for j in slice if j < arr[i]]
        res.append(len(c_res))
    return res
