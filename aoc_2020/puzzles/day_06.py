from functools import reduce


def get_groups():
    with open('../input/day_6.txt') as f:
        return [[{char for char in line} for line in group.splitlines()] for group in f.read().split('\n\n')]


def reducer(groups, fn):
    return sum(len(reduce(fn, sets)) for sets in groups)


def main():
    groups = get_groups()
    print(reducer(groups, set.union))
    print(reducer(groups, set.intersection))


if __name__ == '__main__':
    main()
