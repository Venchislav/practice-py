# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original): return False
    else: return len([i for i in list(test.lower()) if i in list(original.lower())]) == len(test)


# G E N I U S   B R A I N 2

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
