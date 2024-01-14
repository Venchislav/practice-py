def missingNumber(self, nums: List[int]) -> int:
  for num in range(0, max(nums) + 2):
    if not num in nums:
      return num
  return -1
