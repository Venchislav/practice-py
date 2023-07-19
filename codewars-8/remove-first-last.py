def array(string):
    return ' '.join(string.split(',')[1:-1]) if len(string.split(',')[1:-1]) >= 1 else None


# Shorter solution that I didn't know about :|

def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None
