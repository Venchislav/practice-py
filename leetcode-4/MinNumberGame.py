def numberGame(nums):
    arr = []
    while nums != []:    
        a = nums.pop(nums.index(min(nums)))
        b = nums.pop(nums.index(min(nums)))
        arr.append(b)
        arr.append(a)
    return arr


print(numberGame([5, 4, 2, 3]))
print(numberGame([2, 5]))
