def highest_rank(arr):
    max_num = 0
    for i in arr:
        if arr.count(i) > arr.count(max_num):
            max_num = i
        elif arr.count(i) == arr.count(max_num) and i > max_num:
            max_num = i
    return max_num
