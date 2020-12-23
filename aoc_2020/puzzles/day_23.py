def main():
    # pt 1
    nums = [int(n) for n in '167248359']
    for n in range(100):
        nums = play_turn(nums)

    idx = nums.index(1)
    print(*(nums[idx + 1:] + nums[:idx]), sep="")


def play_turn(nums):
    head, move = nums[0], nums[1:4]
    dest = head - 1
    while not dest or dest in move:
        dest -= 1
        dest %= 10
    idx = nums.index(dest)
    assert idx >= 4
    nums = [*nums[4:idx + 1], *move, *nums[idx + 1:], head]
    return nums


if __name__ == '__main__':
    main()
