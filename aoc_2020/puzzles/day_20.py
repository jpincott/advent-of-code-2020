from functools import reduce
from math import prod

from aoc_2020.utils.decorators import timer


class Tile:
    def __init__(self, key, cells):
        self.key = key
        self.cells = cells

    def all_edges(self):
        return [
            t := self.cells[0], t[::-1],
            b := self.cells[-1], b[::-1],
            l := "".join([c[0] for c in self.cells]), l[::-1],
            r := "".join([c[-1] for c in self.cells]), r[::-1],
        ]

    def __repr__(self):
        return self.key


def load_tiles() -> list[Tile]:
    with open('../input/day_20.txt') as f:
        return [
            Tile(int(tile[0][5:-1]), tile[1:])
            for block in f.read().split('\n\n')
            if (tile := block.splitlines())
        ]


@timer
def main():
    # load tiles
    tiles = load_tiles()

    # map edges to tiles
    edges_to_tiles = reduce(
        lambda acc, arg: acc | {arg[0]: acc.get(arg[0], {arg[1]}) | {arg[1]}},
        ((e, t) for t in tiles for e in t.all_edges()),
        {}
    )

    # let's have a look at the distribution of edges
    assert max(len(v) for v in edges_to_tiles.values()) == 2

    # find corners
    corners = {t for t in tiles if sum(len(edges_to_tiles[e]) == 2 for e in t.all_edges()) == 4}

    # Pt 1
    print(prod(c.key for c in corners))


if __name__ == '__main__':
    main()
