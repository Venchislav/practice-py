def mostFrequentEven(nums):
    nums_ = [i for i in nums if i % 2 == 0]
    if len(nums_) == 0:
        return -1
    
    return max(nums_, key=nums_.count) if len(set(nums_)) != len(nums_) else nums_[0]

a = [1, 22, 2, 3, 3, 3, 2]
print(mostFrequentEven(a))
# well  
