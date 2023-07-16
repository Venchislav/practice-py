def small_enough(array, limit):
    return len([i for i in array if i <= limit]) == len(array)


# G E N I U S   B R A I N

def small_enough(array, limit):
    return max(array) <= limit
