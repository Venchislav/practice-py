def isPalindrome(s):
    s = s.lower()
    s = ''.join(s.split())
    s = [i for i in s if i.isalpha() or i.isdigit()]
    return s == s[::-1]


print(isPalindrome("0P"))
