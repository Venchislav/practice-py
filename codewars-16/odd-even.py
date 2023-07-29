def sort_my_string(s):
    s = list(s)
    even = list()
    odd = list()
    for i in range(len(s)):
        if i == 0 or i%2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    return f"{''.join(even)} {''.join(odd)}"


# M E G A   M I N D   M O M E N T


def sort_my_string(s):
    return '{} {}'.format(s[::2], s[1::2])
