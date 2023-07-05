def removeDuplicates(nums):
    # apply to our arr
    nums[:] = sorted(set(nums))
    return len(nums)


print(removeDuplicates([1, 1, 2]))
