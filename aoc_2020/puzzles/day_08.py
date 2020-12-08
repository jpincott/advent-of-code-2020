from aoc_2020.utils.io import stream_lines


def execute(prg):
    acc, ptr = 0, 0
    seen = set()
    while ptr not in seen and ptr < len(prg):
        seen.add(ptr)
        ins, val = prg[ptr].split()
        if ins == 'acc':
            acc += int(val)
            ptr += 1
        if ins == 'jmp':
            ptr += int(val)
        if ins == 'nop':
            ptr += 1
    return acc, ptr


def main():
    prg = [line.strip() for line in stream_lines(day=8)]

    # pt 1
    acc, ptr = execute(prg)
    print(acc)

    # pt 2
    for i in range(len(prg)):
        new_prg = prg.copy()
        if new_prg[i][:3] == 'jmp':
            new_prg[i] = 'nop' + new_prg[i][3:]
        elif new_prg[i][:3] == 'nop':
            new_prg[i] = 'jmp' + new_prg[i][3:]
        acc, ptr = execute(new_prg)
        if ptr == len(prg):
            print(acc)


if __name__ == '__main__':
    main()
