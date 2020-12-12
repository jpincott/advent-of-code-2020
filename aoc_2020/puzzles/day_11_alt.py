from functools import reduce
from itertools import count, takewhile

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


def load_grid():
    return {
        complex(i, j): False
        for i, r in enumerate(stream_lines(day=11))
        for j, c in enumerate(r.strip())
        if c != '.'
    }


def evolve(grid, adj, l):
    return {k: 0 == sum(grid[z] for z in adj[k]) for k, v in grid.items() if not v} | \
           {k: l >= sum(grid[z] for z in adj[k]) for k, v in grid.items() if v}


@timer
def find_neigbours(grid):
    deltas = {complex(re - 1, im - 1) for re in range(3) for im in range(3)} - {0 + 0j}
    return {z: {z + d for d in deltas if z + d in grid} for z in grid}


@timer
def find_ranged(grid):
    deltas = {complex(re - 1, im - 1) for re in range(3) for im in range(3)} - {0 + 0j}
    rows = range(min(int(z.imag) for z in grid), 1 + max(int(z.imag) for z in grid))
    cols = range(min(int(z.real) for z in grid), 1 + max(int(z.real) for z in grid))
    return {z: reduce(set.union, (next(
        ({w} for w in takewhile(lambda x: x.real in cols and x.imag in rows, (z + n * d for n in count(1))) if
         w in grid), set()) for d in deltas)) for z in grid}


@timer
def solve_it(fn, limit):
    grid = load_grid()
    adj = fn(grid)
    prev = None
    while prev != grid:
        prev, grid = grid, evolve(grid, adj, limit)
    return sum(grid.values())


@timer
def main():
    print(solve_it(find_neigbours, 3))
    print(solve_it(find_ranged, 4))


if __name__ == '__main__':
    main()
