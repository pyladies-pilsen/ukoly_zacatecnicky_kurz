from itertools import combinations_with_replacement


def get_neighbours(x, y):
    for a, b in combinations_with_replacement((-1,0,1), 2):
        if (a, b) == (0, 0):
            continue
        yield x + a, y + b