def find_disappeared_numbers(nums):
    return list(set(range(1, len(nums) + 1)).difference(set(nums)))
