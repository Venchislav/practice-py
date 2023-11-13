def rotateString(s, goal):
    s_ = list(s)
    for _ in range(len(s)):
        s_.append(s_[0])
        s_ = s_[1:]
        print(s_)
        if ''.join(s_) == goal:
            return True
    return False


print(rotateString("abcde", "abced"))
# Bruh... I made too much commits in here just because of my absent-mindedness😪

# P.S This code is not the best solution, but it's mine and I made it with my little hands and it performs quiet well (32ms; 13.18MB)
