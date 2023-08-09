def is_isomorphic(self, s, t):
    zipped_set = set(zip(s, t))
    return len(zipped_set) == len(set(s)) == len(set(t))
