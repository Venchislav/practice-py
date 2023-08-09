def is_good(nums):
    return sorted(nums) == list(range(1, max(nums) + 1)) + [max(nums)]
