from collections import Counter

from more_itertools.recipes import pairwise

from aoc_2020.utils.io import stream_lines


def main():
    adapters = sorted(int(n) for n in stream_lines(day=10))

    # pt1
    diffs = Counter(y - x for x, y in pairwise([0] + adapters))
    print(diffs[1] * (1 + diffs[3]))

    # pt 2
    paths = Counter({0: 1})
    for adapter in adapters:
        paths[adapter] = sum(paths[n] for n in range(adapter - 3, adapter))
    print(paths[adapters[-1]])


if __name__ == '__main__':
    main()
