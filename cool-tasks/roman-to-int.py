def romanToInt(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res, prev = 0, 0
    for i in s[::-1]:
        if rom_val[i] >= prev:
            res += rom_val[i]
        else:
            res -= rom_val[i]
        prev = rom_val[i]
    return res


# EXPLANATION BY CHATGPT (traditionally)

"""
This code implements a solution to the problem of converting Roman numbers to integers. In this problem, you are given a string s representing a Roman number, and your task is to convert it to the corresponding integer.

So let's see how this code works.

rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} - We create a rom_val dictionary , in which each Roman numeral (key) corresponds to the corresponding integer (value).

res, prev = 0, 0 - We create the variables res and prev and initialize them to 0. The res variable will contain the resulting integer, and the prev variable will contain the value of the previous Roman numeral.

for i in s[::-1]: - We iterate over each Roman numeral i in string s in reverse order (from the end).

if rom_val[i] >= prev: - We check if the value of the current roman numeral i is greater than or equal to the value of the previous roman numeral (prev), then add that value to the result (res).

else: - Otherwise (if the value of the current roman numeral i is less than the value of the previous roman numeral), we subtract the value of the current roman numeral from the result (res).

prev = rom_val[i] - We update the value of the variable prev with the corresponding value of the current roman numeral.

return res - After the loop completes, we return the final value res, which is the converted integer for the given Roman numeric string.
"""
