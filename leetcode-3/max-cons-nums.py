def find_max_consecutive_ones(nums):
    return len(max(''.join([str(i) for i in nums]).split('0')))
