def replace_exclamation(s):
    vowels = 'AEIOUaeiou'
    for i in vowels: s = s.replace(i, '!')
    return s
