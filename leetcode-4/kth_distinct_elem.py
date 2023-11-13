s_ = list(s)
    for _ in range(len(s)):
        s_.append(s_[0])
        s_ = s_[1:]
        print(s_)
        if ''.join(s_) == goal:
            return True
    return False
