from more_itertools import powerset

from aoc_2020.utils.io import stream_lines


def load_program():
    return [l.strip().split(' = ') for l in stream_lines(day=14)]


def apply(mask, val):
    val |= int(mask.replace('X', '0'), 2)
    val &= int(mask.replace('X', '1'), 2)
    return val


def stream_addresses(mask, loc):
    loc |= int(mask.replace('X', '0'), 2)
    loc &= int(mask.replace('0', '1').replace('X', '0'), 2)
    return (loc | sum(s) for s in powerset(1 << i for i, c in enumerate(mask[::-1]) if c == 'X'))


def main():
    prg = load_program()

    # pt 1
    mem = write_masked_value_to_location(prg)
    print(sum(mem.values()))

    # pt 2
    mem = write_value_to_masked_locations(prg)
    print(sum(mem.values()))


def write_masked_value_to_location(prg):
    mask, mem = 0, {}
    for cmd, arg in prg:
        if cmd == 'mask':
            mask = arg
        else:
            mem[cmd[4:-1]] = apply(mask, int(arg))
    return mem


def write_value_to_masked_locations(prg):
    mask, mem = 0, {}
    for cmd, arg in prg:
        if cmd == 'mask':
            mask = arg
        else:
            mem |= {addr: int(arg) for addr in stream_addresses(mask, int(cmd[4:-1]))}
    return mem


if __name__ == '__main__':
    main()
