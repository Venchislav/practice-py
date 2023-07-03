"""
def twoSum(nums, target):
    for elem in nums:
        if target - elem in nums:
            return [nums.index(elem)] + [nums.index(target - elem)]
    return -1


print(twoSum([1, 3, 4, 2], 7))
"""


def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            sorted([i, seen[remaining]])
        else:
            seen[value] = i
    return seen


print(twoSum([3, 3, 2, 1], 9))
