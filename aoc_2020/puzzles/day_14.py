from more_itertools import powerset

from aoc_2020.utils.io import stream_lines


def load_program():
    return [
        (cmd, arg) if cmd == 'mask' else (int(cmd[4:-1]), int(arg))
        for cmd, arg in (l.strip().split(' = ') for l in stream_lines(day=14))
    ]


def execute(prg, fn):
    # functional version is slower:
    # return reduce(lambda a, t: (t[1], a[1]) if t[0] == 'mask' else (a[0], a[1] | fn(a[0], *t)), prg, (0, {}))[1]
    mask, mem = 0, {}
    for cmd, arg in prg:
        if cmd == 'mask':
            mask = arg
        else:
            mem |= fn(mask, cmd, arg)
    return mem


def apply(mask, val):
    val |= int(mask.replace('X', '0'), 2)
    val &= int(mask.replace('X', '1'), 2)
    return val


def gen_locations(mask, loc):
    loc |= int(mask.replace('X', '0'), 2)
    loc &= int(mask.replace('0', '1').replace('X', '0'), 2)
    return (loc | sum(s) for s in powerset(1 << i for i, c in enumerate(mask[::-1]) if c == 'X'))


def main():
    prg = load_program()

    # pt 1
    mem = execute(prg, lambda mask, loc, val: {loc: apply(mask, val)})
    print(sum(mem.values()))

    # pt 2
    mem = execute(prg, lambda mask, loc, val: {loc: val for loc in gen_locations(mask, loc)})
    print(sum(mem.values()))


if __name__ == '__main__':
    main()
