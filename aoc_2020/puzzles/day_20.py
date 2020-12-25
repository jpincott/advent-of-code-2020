from functools import reduce
from math import prod, isqrt

from more_itertools import first
from more_itertools.more import one

from aoc_2020.utils.decorators import timer


class Tile:
    def __init__(self, key, cells):
        self.key = key
        self.cells = cells
        self.h = len(cells)
        self.w = len(cells[0])
        assert all(self.w == len(r) for r in cells)

    def __repr__(self):
        return str(self.key)

    def all_edges(self):
        return [
            t := self.cells[0], t[::-1],
            b := self.cells[-1], b[::-1],
            l := "".join([c[0] for c in self.cells]), l[::-1],
            r := "".join([c[-1] for c in self.cells]), r[::-1],
        ]

    def top(self):
        return self.cells[0]

    def bottom(self):
        return self.cells[-1]

    def left(self):
        return "".join([c[0] for c in self.cells])

    def right(self):
        return "".join([c[-1] for c in self.cells])

    def rotate(self):
        new = [[None] * self.h for _ in range(self.w)]
        for r in range(self.h):
            for c in range(self.w):
                new[self.w - c - 1][r] = self.cells[r][c]
        for r in range(self.w):
            new[r] = ''.join(new[r])
        self.cells = new
        self.h, self.w = self.w, self.h
        return self

    def vflip(self):
        new = [r[::-1] for r in self.cells]
        self.cells = new
        return self

    def hflip(self):
        new = [r for r in self.cells[::-1]]
        self.cells = new
        return self


def load_tiles() -> list[Tile]:
    with open('../input/day_20.txt') as f:
        return [
            Tile((key := int(tile[0][5:-1])), tile[1:])
            for block in f.read().split('\n\n')
            if (tile := block.splitlines())
        ]


def get_neigbour(tile, edge, edges):
    return one(edges[edge] - {tile})


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

    # classify edges
    internal_edges = {e for e, l in edges_to_tiles.items() if len(l) == 2}
    external_edges = {e for e, l in edges_to_tiles.items() if len(l) == 1}

    # find corners
    corners = {t for t in tiles if sum(e in internal_edges for e in t.all_edges()) == 4}

    # Pt 1
    print(prod(c.key for c in corners))

    # Pt 2
    # Pick a corner
    t = first(corners)

    # orient it to place at (0,0)
    n = isqrt(len(tiles))
    grid = [[None] * n for i in range(n)]
    grid[0][0] = t
    while t.bottom() not in internal_edges:
        t.rotate()
    while t.right() not in internal_edges:
        t.vflip()

    # fill down
    for r in range(1, n):
        # find neighbouring tile
        t = grid[r - 1][0]
        e = t.bottom()
        t = get_neigbour(t, e, edges_to_tiles)

        # orient
        while t.top() not in (e, e[::-1]):
            t.rotate()
        if t.top() != e:
            t.vflip()
        grid[r][0] = t

    # fill across
    for r in range(n):
        for c in range(1, n):
            t = grid[r][c - 1]
            e = t.right()
            t = get_neigbour(t, e, edges_to_tiles)

            while t.left() not in (e, e[::-1]):
                t.rotate()
            if t.left() != e:
                t.hflip()
            grid[r][c] = t

    # assemble picture
    cells = []
    for r in range(n):
        for rr in range(1, t.h - 1):
            row = []
            for c in range(n):
                row.extend(grid[r][c].cells[rr][1:-1])
            cells.append(row)

    grid = Tile('grid', cells)

    # find monsters
    monster = Tile('monster', [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ])

    # rotate and flip
    m = 0
    for f in range(2):
        for r in range(4):
            m += count_monsters(grid, monster)
            grid.rotate()
        grid.vflip()

    roughness = sum(c == '#' for r in grid.cells for c in r) - m * sum(c == '#' for r in monster.cells for c in r)
    print(roughness)


def count_monsters(grid, monster):
    return sum(
        all(grid.cells[rg + rm][cg + cm] == '#'
            for rm in range(monster.h)
            for cm in range(monster.w)
            if monster.cells[rm][cm] == '#')
        for rg in range(grid.h - monster.h)
        for cg in range(grid.w - monster.w)
    )


if __name__ == '__main__':
    main()
