from parse import parse

from aoc_2020.utils.decorators import timer
from aoc_2020.utils.io import stream_lines


class VM:
    ops = {
        'nop': lambda arg, acc, ptr: (acc, ptr + 1),
        'jmp': lambda arg, acc, ptr: (acc, ptr + arg),
        'acc': lambda arg, acc, ptr: (acc + arg, ptr + 1)
    }

    def __init__(self):
        self.acc = 0
        self.ptr = 0

    def run(self, prg):
        cache = set()
        while self.ptr not in cache and self.ptr < len(prg):
            cache.add(self.ptr)
            op, arg = prg[self.ptr]
            self.acc, self.ptr = self.ops[op](arg, self.acc, self.ptr)
        return self.acc, self.ptr == len(prg)


@timer
def main():
    prg = [parse("{} {:d}", line).fixed for line in stream_lines(day=8)]

    # pt 1
    acc, _ = VM().run(prg)
    print(acc)

    # pt 2
    fix = lambda op, arg: ({'nop': 'jmp', 'jmp': 'nop'}[op], arg)
    print(next(
        acc
        for i in range(len(prg)) if not prg[i][0] == 'acc'
        for acc, status in [VM().run([fix(*ins) if i == j else ins for j, ins in enumerate(prg)])]
        if status
    ))


if __name__ == '__main__':
    main()
