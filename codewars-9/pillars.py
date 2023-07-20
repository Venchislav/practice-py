def pillars(num_pill, dist, width):
    return 0 if num_pill < 2 else num_pill * ((dist * 100) + width) - (width * 2) - (dist * 100)
