def find_complement(num):
    os = 0
    numb = str(bin(num)[2:]).format(6)
    num = ''.join('0' if i == '1' else '1' for i in numb)
    return int(num, 2)
    
    
print(find_complement(1))
print(find_complement(5))

# link: https://leetcode.com/problems/number-complement/
