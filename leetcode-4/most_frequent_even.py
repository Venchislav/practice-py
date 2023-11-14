def mostFrequentEven(nums):
    nums_ = [i for i in nums if i % 2 == 0]
    if len(nums_) == 0:
        return -1
    
    return max(nums_, key=nums_.count) if len(set(nums_)) != len(nums_) else nums_[0]

a = [1, 22, 2, 3, 3, 3, 2]
print(mostFrequentEven(a))
# well
# my solution is not 100% correct for leetcode...
# so there's another solution

class Solution(object):
    def mostFrequentEven(self, nums):
        seen = {}
        for item in nums:
            if item % 2 ==0:
                seen[item] = 1 if item not in seen else seen[item] + 1
        maxx = 0    
        output = -1        
        for num, count in seen.items():
            if count > maxx:
                maxx, output = count, num
            elif count == maxx:
                output = min(num,output)
        return output


        
