def enough(cap, on, wait):
    return on + wait - cap if cap - (on + wait) < 0 else 0


# but better

def enough(cap, on, wait):
    return max(0, wait - (cap - on))
