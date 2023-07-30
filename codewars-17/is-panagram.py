def is_pangram(s):
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s.lower():
            return False
    return True
