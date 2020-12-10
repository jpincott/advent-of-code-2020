from itertools import combinations

from more_itertools import windowed

from aoc_2020.utils.io import stream_lines


def main():
    nums = [int(n) for n in stream_lines(day=9)]
    window = 25

    pt1 = next(
        nums[window + i]
        for i, w in enumerate(windowed(nums, window))
        if all(x + y != nums[i + window] for x, y in combinations(w, 2))
    )

    print(pt1)

    pt2 = next(
        min(w) + max(w)
        for l in range(2, len(nums))
        for w in windowed(nums, l)
        if sum(w) == pt1
    )

    print(pt2)


if __name__ == '__main__':
    main()
