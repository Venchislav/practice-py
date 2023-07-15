def capitalize(s):
    r = ''
    x = ''
    b = True
    for c in s:
        r += c.upper() if b else c.lower()
        x += c.lower() if b else c.upper()
        if c.isalpha():
            b = not b
    return [r, x]

# G E N I U S B R A I N

def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
