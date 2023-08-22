def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [i, nums.index(target - nums[i])]
        else:
            seen[nums[i]] = i
