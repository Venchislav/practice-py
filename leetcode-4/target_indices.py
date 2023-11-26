nums = sorted(nums)
    arr = []
    for n in range(len(nums)):
        if nums[n] == target:
            arr.append(n)
    return arr


print(targetIndices([1,2,5,2,3], 2))
