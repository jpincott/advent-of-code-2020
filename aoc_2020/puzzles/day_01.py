from itertools import combinations
from math import prod

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


@timer
def find(nums, size):
    return next(prod(t) for t in combinations(nums, size) if sum(t) == 2020)


def main():
    nums = {int(s) for s in stream_lines(day=1)}
    print(find(nums, 2))
    print(find(nums, 3))


if __name__ == '__main__':
    main()
