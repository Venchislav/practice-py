def reverse_letter(string):
    for elem in list(string):
        if not elem.isalpha():
            string = string.replace(elem, '')
    return string[::-1]


print(reverse_letter('ultr53o?n'))
