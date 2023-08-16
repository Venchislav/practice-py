def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


# explained by ChatGpt:
"""
This code implements a solution to the problem known as "Single Number". In this problem, you are given an array nums, in which all elements appear twice, except for one element, which appears only once. The task is to find and return this unique element.

So let's see how this code works.

a = 0 - We create a variable a and initialize it to 0. This variable will be used to perform a bitwise exclusive OR (XOR) operation.

for i in nums: - We iterate over each i element in the nums array.

a ^= i - We perform a bitwise XOR (^=) between the variable a and the current element i. The XOR operation returns 1 when the bits are in different states and 0 when the bits are in the same state. Essentially, this operation "adds" the bits of each element of the nums array and finally finds a unique element, since duplicate elements will cancel each other out.

return a - After the loop is completed, we have the result of the XOR operation of all elements of the nums array. This will be the value of the unique element in the array, since duplicate elements cancel each other out.

It follows that the singleNumber function takes an array of nums and performs an XOR operation on each element of the array, which allows you to find a unique element that appears only once.
"""