from collections import Counter
from functools import cache
from itertools import takewhile

from more_itertools.recipes import pairwise

from aoc_2020.utils.io import stream_lines


@cache
def count_paths(adaptors, start=0):
    if start == len(adaptors) - 1:
        return 1

    return sum(
        count_paths(adaptors, i)
        for i in takewhile(
            lambda n: adaptors[n] - adaptors[start] <= 3,
            range(start + 1, len(adaptors))
        )
    )


def main():
    adapters = sorted([int(n) for n in stream_lines(day=10)])
    adapters = (0, *adapters, adapters[-1] + 3)

    # pt1
    diffs = Counter(y - x for x, y in pairwise(adapters))
    print(diffs[1] * diffs[3])

    # pt 2
    paths = count_paths(adapters)
    print(paths)


if __name__ == '__main__':
    main()
