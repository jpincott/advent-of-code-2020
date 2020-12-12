from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


def load_grid():
    return (rows := [l.strip() for l in stream_lines(day=11)]), len(rows), len(rows[0])


def evolve(grid, rows, cols):
    nextgrid = []
    for r in range(rows):
        col = ''
        for c in range(cols):
            n = 0
            s = grid[r][c]
            for dr in range(max(0, r - 1), min(r + 2, rows)):
                for dc in range(max(0, c - 1), min(c + 2, cols)):
                    if not (r == dr and c == dc):
                        n += grid[dr][dc] == '#'
            if s == '#' and n >= 4:
                col += 'L'
            elif s == 'L' and n == 0:
                col += '#'
            else:
                col += s
        nextgrid.append(col)

    return tuple(nextgrid)


def walkit(grid, rows, cols, r, c, dr, dc):
    r += dr
    c += dc
    if r not in range(rows) or c not in range(cols):
        return None

    return s if '.' != (s := grid[r][c]) else walkit(grid, rows, cols, r, c, dr, dc)


def evolve2(grid, rows, cols):
    nextgrid = []
    for r in range(rows):
        col = ''
        for c in range(cols):
            n = 0
            s = grid[r][c]
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr == 0 and dc == 0):
                        n += walkit(grid, rows, cols, r, c, dr, dc) == '#'
            if s == '#' and n >= 5:
                col += 'L'
            elif s == 'L' and n == 0:
                col += '#'
            else:
                col += s
        nextgrid.append(col)

    return nextgrid


@timer
def main():
    # pt 1
    grid, rows, cols = load_grid()
    prev = None
    while prev != grid:
        prev, grid = grid, evolve(grid, rows, cols)

    print(sum(r.count('#') for r in grid))

    # pt 2
    grid, rows, cols = load_grid()
    prev = None
    while prev != grid:
        prev, grid = grid, evolve2(grid, rows, cols)

    print(sum(r.count('#') for r in grid))


if __name__ == '__main__':
    main()
