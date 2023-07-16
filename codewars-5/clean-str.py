def string_clean(s):
    for i in list(s):
        if i in '0123456789': s = s.replace(i, '')
    return s


# better

def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
