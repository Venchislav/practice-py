def check_exam(arr1, arr2):
    res = 0
    for i in range(len(arr1)):
        if arr2[i] == arr1[i]:
            res += 4
        elif arr2[i] == "":
            res -= 0
        else:
            res -= 1
    return res if res > 0 else 0
