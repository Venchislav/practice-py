def remove(s):
    if len(s) < 1:
        return s
    if list(s)[-1] == '!':
        return s[:-1]
    else:
        return s
