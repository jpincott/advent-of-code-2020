import re
from collections import Counter

from aoc_2020.utils.io import stream_lines


def get_input():
    return [re.findall(r'(sw|se|nw|ne|w|e)', l) for l in stream_lines(day=24)]


def to_coords(steps):
    c = Counter(steps)
    ne, e, se = c['ne'] - c['sw'], c['e'] - c['w'], c['se'] - c['nw']
    return ne + e, se + e


def neighbours(c):
    return {tuple(map(sum, zip(c, d))) for d in ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))}


def evolve(cells):
    next_gen = set()  # results'
    boundary = Counter()  # all cells to consider for next gen

    # check all active cells
    for c in cells:
        # find all 6 neighbours (excludes self)
        n = neighbours(c)

        # add empty neighbours to boundary
        boundary.update(n - cells)

        # count active neighbours
        s = len(n & cells)

        # propagate to next gen if 1 or 2 neighbours
        if s in (1, 2):
            next_gen.add(c)

    # check empty cells
    # propagate to next gen if 2 neighbours
    next_gen.update({c for c, v in boundary.items() if v == 2})

    # we're done
    return next_gen


def main():
    input = get_input()
    coords = [to_coords(steps) for steps in input]

    # pt 1
    print(sum(v % 2 for v in Counter(coords).values()))

    # pt 2
    cells = {c for c, v in Counter(coords).items() if v % 2}
    for _ in range(100):
        cells = evolve(cells)
    print(len(cells))


if __name__ == '__main__':
    main()
