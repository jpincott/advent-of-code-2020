from functools import reduce

from aoc_2020.utils.io import stream_lines


def main():
    actions = [(line[0], int(line[1:])) for line in stream_lines(day=12)]

    # pt 1
    fns = {
        'F': lambda x, v, n: (x + n * v, v),
        'N': lambda x, v, n: (x + n * 1j, v),
        'S': lambda x, v, n: (x - n * 1j, v),
        'E': lambda x, v, n: (x + n, v),
        'W': lambda x, v, n: (x - n, v),
        'R': lambda x, v, n: (x, v * pow(-1j, n // 90)),
        'L': lambda x, v, n: (x, v * pow(1j, n // 90))
    }

    ship, _ = perform_actions(actions, fns, 0, 1)
    print(abs(ship.real) + abs(ship.imag))

    # pt2
    fns |= {
        'N': lambda x, v, n: (x, v + n * 1j),
        'S': lambda x, v, n: (x, v - n * 1j),
        'E': lambda x, v, n: (x, v + n),
        'W': lambda x, v, n: (x, v - n),
    }

    ship, _ = perform_actions(actions, fns, 0, 10 + 1j)
    print(abs(ship.real) + abs(ship.imag))


def perform_actions(actions, functions, start, heading):
    return reduce(lambda acc, a: functions[a[0]](*acc, a[1]), actions, (start, heading))


if __name__ == '__main__':
    main()
