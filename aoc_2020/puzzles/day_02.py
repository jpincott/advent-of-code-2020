from functools import reduce

from parse import parse

from aoc_2020.utils.io import stream_lines


def main():
    pt1 = lambda min, max, char, string: string.count(char) in range(min, max + 1)
    pt2 = lambda i, j, char, string: (string[i - 1] == char) ^ (string[j - 1] == char)
    print(*reduce(
        lambda acc, args: map(sum, zip(acc, (pt1(*args), pt2(*args)))),
        (parse("{:d}-{:d} {}: {}", line).fixed for line in stream_lines(day=2)),
        (0, 0)
    ))


if __name__ == '__main__':
    main()
