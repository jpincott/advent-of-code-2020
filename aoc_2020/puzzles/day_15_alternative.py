from collections import defaultdict

from aoc_2020.utils.decorators import timer


def get_nums():
    nums = [int(i) for i in '18,11,9,0,5,1'.split(',')]
    return defaultdict(lambda: [], {n: [i + 1] for i, n in enumerate(nums)}), nums[-1], len(nums)


def main():
    print(solve_it(2020))
    print(solve_it(30000000))


@timer
def solve_it(limit):
    nums, last, turns = get_nums()
    for turn in range(turns, limit):
        hist = nums[last]
        nums[last].append(turn)
        last = 0 if len(hist) == 1 else turn - nums[last][-2]
    return last


if __name__ == '__main__':
    main()
