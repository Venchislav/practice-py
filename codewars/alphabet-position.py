def alphabet_position(text):
    res = ''
    for elem in text:
        if elem.isalpha():
            res += str(ord(elem.lower())-96)
            res += ' '
    return res.rstrip()


print(alphabet_position("The sunset sets at twelve o' clock."))
