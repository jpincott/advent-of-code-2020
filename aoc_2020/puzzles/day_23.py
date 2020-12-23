from itertools import accumulate
from math import prod


def main():
    nums = [int(n) for n in '167248359']

    # pt 1
    pt1 = play_game(nums)
    idx = pt1.index(1)
    print(*pt1[idx + 1:], *pt1[:idx], sep="")

    # pt 2(a) check same answer for pt 1
    pt2 = play_big_game(nums)
    print(*accumulate(range(len(pt1) - 2), lambda c, _: pt2[c], initial=pt2[1]), sep='')

    pt2 = play_big_game(nums + list(range(len(nums) + 1, 1_000_000 + 1)), turns=10_000_000)
    print(prod(accumulate(range(1), lambda c, _: pt2[c], initial=pt2[1])))


def play_game(nums, turns=100):
    for _ in range(turns):
        head, move = nums[0], nums[1:4]
        dest = get_dest(head, move, nums)
        idx = nums.index(dest) + 1
        nums = [*nums[4:idx], *move, *nums[idx:], head]
    return nums


def play_big_game(nums, turns=100):
    link = dict(zip(nums, nums[1:] + nums[:1]))
    head = nums[-1]
    for _ in range(turns):
        head = link[head]
        move = list(accumulate(range(2), lambda c, _: link[c], initial=link[head]))
        dest = get_dest(head, move, nums)
        link[head], link[move[-1]], link[dest] = link[move[-1]], link[dest], move[0]
    return link


def get_dest(curr, move, nums):
    dest = curr - 1
    while not dest or dest in move:
        dest = (dest - 1) % (len(nums) + 1)
    return dest


if __name__ == '__main__':
    main()
