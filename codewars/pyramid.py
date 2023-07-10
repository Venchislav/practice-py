def tower_builder(n_floors):
    tower = []
    floor = ''

    for i in range(n_floors):
        stars = '*' * (i * 2 + 1)
        spaces = ' ' * (n_floors - i - 1)
        floor = spaces + stars + spaces
        tower.append(floor)

    return tower
