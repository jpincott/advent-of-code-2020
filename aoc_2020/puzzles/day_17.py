from functools import cache
from itertools import product

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


def get_input(d):
    return {(x, y) + (0,) * (d - 2) for y, r in enumerate(stream_lines(day=17)) for x, c in enumerate(r) if c == '#'}


@cache
def neighbours(c):
    return {tuple(map(sum, zip(c, d))) for d in product((-1, 0, 1), repeat=len(c))}


def evolve(cells):
    next_gen = set()  # results'
    boundary = set()  # all cells to consider for next gen

    # check all active cells
    for c in cells:
        # find all 3**n neighbours (includes self)
        n = neighbours(c)

        # add empty neighbours to boundary
        boundary |= (n - cells)

        # count active neighbours
        s = len(n & cells) - 1

        # propagate to next gen if 2 or 3 neighbours
        if s in (2, 3):
            next_gen.add(c)

    # check empty cells
    for c in boundary - cells:
        # find all 3**n neighbours (includes self)
        n = neighbours(c)

        # count active neighbours
        s = len(n & cells)

        # propagate to next gen if 3 neighbours
        if s == 3:
            next_gen.add(c)

    # we're done
    return next_gen


@timer
def main():
    # pt 1
    cells = get_input(3)
    for t in range(6):
        cells = evolve(cells)
    print(len(cells))

    # pt 2
    cells = get_input(4)
    for t in range(6):
        cells = evolve(cells)
    print(len(cells))


if __name__ == '__main__':
    main()
