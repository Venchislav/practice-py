def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)


# longer

def to_csv_text(array):
    res = ''
    for i in array:
        res += str(i) + '\n'
    return res.replace('[', '').replace(']', '').replace(' ', '')[:-1]
