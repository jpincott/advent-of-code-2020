from collections import defaultdict

from aoc_2020.utils.decorators import timer


def get_nums():
    nums = [int(i) for i in '18,11,9,0,5,1'.split(',')]
    return defaultdict(lambda: 0, {n: i + 1 for i, n in enumerate(nums)}), nums[-1], len(nums)


def main():
    print(solve_it(2020))
    print(solve_it(30000000))


@timer
def solve_it(limit):
    nums, last, turns = get_nums()
    for turn in range(turns, limit):
        nums[last], last = turn, 0 if nums[last] == 0 else turn - nums[last]
    return last


if __name__ == '__main__':
    main()
