from functools import reduce

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


@timer
def main():
    actions = [(line[0], int(line[1:])) for line in stream_lines(day=12)]

    # pt 1
    fns = {
        'F': lambda x, v, d, n: (x + n * v, v),
        'N': lambda x, v, d, n: (x + n * 1j, v),
        'S': lambda x, v, d, n: (x - n * 1j, v),
        'E': lambda x, v, d, n: (x + n, v),
        'W': lambda x, v, d, n: (x - n, v),
        'R': lambda x, v, d, n: (x, v * pow(-1j, n // 90)),
        'L': lambda x, v, d, n: (x, v * pow(1j, n // 90))
    }

    ship, _ = reduce(lambda acc, a: fns[a[0]](*acc, *a), actions, (0, 1))
    print(abs(ship.real) + abs(ship.imag))

    # pt2
    fns |= {
        'N': lambda x, v, i, n: (x, v + n * 1j),
        'S': lambda x, v, i, n: (x, v - n * 1j),
        'E': lambda x, v, i, n: (x, v + n),
        'W': lambda x, v, i, n: (x, v - n),
    }

    ship, _ = reduce(lambda acc, a: fns[a[0]](*acc, *a), actions, (0, 10 + 1j))
    print(abs(ship.real) + abs(ship.imag))


if __name__ == '__main__':
    main()
