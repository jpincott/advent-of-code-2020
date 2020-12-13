from math import prod

from aoc_2020.utils.io import stream_lines


def get_input():
    lines = stream_lines(day=13)
    return int(next(lines)), [int(c) if c != 'x' else c for c in next(lines).strip().split(',')]


def main():
    target, buses = get_input()

    # pt 1
    wait_times = [(b, b - target % b) for b in buses if b != 'x']
    print(prod(min(wait_times, key=lambda t: t[1])))

    # pt 2 (use CRT)
    res_mod = [(-i, b) for i, b in enumerate(buses) if b != 'x']
    N = prod(t[1] for t in res_mod)
    y = sum(r * (n := N // m) * pow(n, -1, m) for r, m in res_mod) % N
    print(y)


if __name__ == '__main__':
    main()
