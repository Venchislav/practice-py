def fake_bin(x):
    result = ""
    string_num = list(x)
    for digit in string_num:
        if int(digit) >= 5:
            result += "1"
        if int(digit) < 5:
            result += "0"
    return result


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)

