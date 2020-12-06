from aoc_2020.utils.io import stream_lines


def calc_id(line):
    binstr = line.translate(str.maketrans('FBRL', '0110'))
    return int(binstr, 2)


def find_missing(passes):
    for n in range(max(passes), 0, -1):
        if n not in passes:
            return n


def main():
    passes = {calc_id(l) for l in stream_lines(day=5)}
    max_val = max(passes)
    print(max_val)
    missing = find_missing(passes)
    print(missing)


if __name__ == '__main__':
    main()
