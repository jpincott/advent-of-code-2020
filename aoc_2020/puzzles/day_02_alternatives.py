from collections import Counter
from dataclasses import dataclass
from functools import reduce
from re import compile, match

import parse

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


@timer
def main():
    pt1, pt2 = 0, 0
    for line in stream_lines(day=2):
        min, max, char, password = match(r"(\d+)-(\d+)\s(\w):\s(.+)", line).groups()
        if Counter(password)[char] in range(int(min), int(max) + 1):
            pt1 += 1
        if (password[int(min)-1] == char) != (password[int(max)-1] == char):
            pt2 += 1
    print(pt1, pt2)


@timer
def main2():
    pattern = compile(r"(\d+)-(\d+)\s(\w):\s(.+)")
    mapper = lambda t: (int(t[0]), int(t[1]), *t[2:])
    parsed = [mapper(pattern.match(line).groups()) for line in (stream_lines(day=2))]

    pt1 = lambda t: Counter(t[3])[t[2]] in range(t[0], t[1] + 1)
    print(sum(map(pt1, parsed)))

    pt2 = lambda t: (t[3][t[0] - 1] == t[2]) != (t[3][t[1] - 1] == t[2])
    print(sum(map(pt2, parsed)))


@timer
def main3():
    pattern = compile(r"(?P<n>\d+)-(?P<m>\d+)\s(?P<c>\w):\s(?P<p>\w+)")
    mapper = lambda d: d | {'n': int(d['n']), 'm': int(d['m'])}

    parsed = [mapper(pattern.match(line).groupdict()) for line in (stream_lines(day=2))]

    pt1 = lambda d: Counter(d['p'])[d['c']] in range(d['n'], d['m'] + 1)
    print(sum(map(pt1, parsed)))

    pt2 = lambda d: (d['p'][d['n'] - 1] == d['c']) != (d['p'][d['m'] - 1] == d['c'])
    print(sum(map(pt2, parsed)))


@dataclass
class Params:
    n: int
    m: int
    char: str
    password: str

    def __init__(self, start, end, char, password):
        self.n = int(start)
        self.m = int(end)
        self.char = char
        self.password = password


@timer
def main4():
    pattern = compile(r"(\d+)-(\d+)\s(\w):\s(.+)")
    parsed = [Params(*pattern.match(line).groups()) for line in (stream_lines(day=2))]

    pt1 = lambda p: Counter(p.password)[p.char] in range(p.n, p.m + 1)
    print(sum(map(pt1, parsed)))

    pt2 = lambda p: (p.password[p.n - 1] == p.char) != (p.password[p.m - 1] == p.char)
    print(sum(map(pt2, parsed)))


@timer
def main5():
    pattern = compile(r"(\d+)-(\d+)\s(\w):\s(.+)")
    parsed = [pattern.match(line).groups() for line in (stream_lines(day=2))]
    pt1 = lambda t: Counter(t[3])[t[2]] in range(int(t[0]), int(t[1]) + 1)
    pt2 = lambda t: (t[3][int(t[0]) - 1] == t[2]) != (t[3][int(t[1]) - 1] == t[2])

    tups = reduce(
        lambda acc, t: ((*acc[0], (pt1(t))), (*acc[1], (pt2(t)))),
        parsed,
        ((), ())
    )
    print(list(map(sum, tups)))


@timer
def main6():
    pattern = compile(r"(\d+)-(\d+)\s(\w):\s(.+)")
    parsed = [pattern.match(line).groups() for line in (stream_lines(day=2))]
    pt1 = lambda t: Counter(t[3])[t[2]] in range(int(t[0]), int(t[1]) + 1)
    pt2 = lambda t: (t[3][int(t[0]) - 1] == t[2]) != (t[3][int(t[1]) - 1] == t[2])
    print(reduce(lambda acc, t: (acc[0] + pt1(t), acc[1] + pt2(t)), parsed, (0, 0)))


@timer
def main7():
    print(
        reduce(
            lambda acc, t: (
                acc[0] + (Counter(t[3])[t[2]] in range(int(t[0]), int(t[1]) + 1)),
                acc[1] + ((t[3][int(t[0]) - 1] == t[2]) != (t[3][int(t[1]) - 1] == t[2]))
            ),
            (match(r"(\d+)-(\d+)\s(\w):\s(.+)", line).groups() for line in stream_lines(day=2)),
            (0, 0)
        )
    )


@timer
def main8():
    lines = stream_lines(day=2)
    pt1, pt2 = 0, 0
    p = parse.compile("{:d}-{:d} {}: {}")
    for l in lines:
        r = p.parse(l)
        min, max, char, password = r.fixed

        if Counter(password)[char] in range(int(min), int(max) + 1):
            pt1 += 1
        if (password[int(min) - 1] == char) != (password[int(max) - 1] == char):
            pt2 += 1
    print(pt1, pt2)


@timer
def main9():
    def pt1(min, max, char, string):
        return Counter(string)[char] in range(min, max + 1)

    def pt2(i, j, char, string):
        return (string[i - 1] == char) ^ (string[j - 1] == char)

    return reduce(
        lambda acc, args: map(sum, zip(acc, (pt1(*args), pt2(*args)))),
        (parse.parse("{:d}-{:d} {}: {}", line).fixed for line in stream_lines(day=2)),
        (0, 0)
    )

if __name__ == '__main__':
    main()
    main2()
    main3()
    main4()
    main5()
    main6()
    main7()
    main8()
    print(*main9())
