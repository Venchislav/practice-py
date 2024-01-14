def missingNumber(self, nums: List[int]) -> int:
  for num in range(min(nums), max(nums) + 2):
    if not num in nums:
      return num
  return -1
