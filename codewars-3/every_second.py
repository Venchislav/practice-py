def remove_every_other(my_list):
    return [my_list[x] for x in range(0, len(my_list), 2)]


# but better

def remove_every_other(my_list):
    return my_list[::2]
