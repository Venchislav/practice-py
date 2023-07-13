def remove_smallest(numbers):
    if len(numbers) < 2:
        return []
    else:
        nums = numbers.copy()
        nums.remove(min(numbers))
        return nums
    