def search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = lo + hi

        if nums[mid] == target:
            return mid
        elif nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
