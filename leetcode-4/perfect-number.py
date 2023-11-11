import math

class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        sum_of_factor = 1
        
        for i in range(2, int(math.floor(num ** 0.5) + 1)):
            if num % i == 0:
                if i == num // i :
                    sum_of_factor +=  i   
                else:
                    sum_of_factor += ( i + num // i )

        return sum_of_factor == num
        
