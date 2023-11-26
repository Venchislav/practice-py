nums = sorted(nums)
    arr = []
    for n in range(len(nums)):
        if nums[n] == target:
            arr.append(n)
    return arr
