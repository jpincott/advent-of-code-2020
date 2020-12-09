from itertools import combinations

from more_itertools import windowed

from aoc_2020.utils.io import stream_lines


def main():
    nums = [int(n) for n in stream_lines(day=9)]
    p = 25

    n = next(
        nums[p + i]
        for i, w in enumerate(windowed(nums, p))
        if all(x + y != nums[i + p] for x, y in combinations(w, 2))
    )

    print(n)

    m = next(
        min(w) + max(w)
        for l in range(2, len(nums))
        for w in windowed(nums, l)
        if sum(w) == n
    )

    print(m)


if __name__ == '__main__':
    main()
