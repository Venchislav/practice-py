def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    l_res = 0
    r_res = 0

    for c in fight:
        if c in left:
            l_res += left[c]
        elif c in right:
            r_res += right[c]
    return "Right side wins!" if r_res > l_res else "Left side wins!" if l_res > r_res else "Let's fight again!"


# Shorter and easier solution

def alphabet_war(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format("Left" if result < 0 else "Right") if result else "Let's fight again!"
