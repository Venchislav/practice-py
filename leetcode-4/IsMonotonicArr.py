def is_monotonic(nums):
    return all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))\
    or all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
