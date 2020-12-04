from functools import partial
from itertools import starmap
from math import prod

from aoc_2020.utils.io import stream_lines


def get_input():
    return [row.strip() for row in stream_lines(3)]


def count_trees(grid, row_step, col_step):
    rows, cols, row, col, trees = len(grid), len(grid[0]), 0, 0, 0
    while row < rows:
        trees += grid[row][col % cols] == '#'
        row += row_step
        col += col_step
    return trees


def main():
    grid = get_input()
    print(count_trees(grid, 1, 3))
    print(prod(starmap(partial(count_trees, grid), [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)])))


if __name__ == '__main__':
    main()
