from aoc_2020.utils.io import stream_lines


def calc_id(line):
    return int(line.translate(str.maketrans('FBRL', '0110')), 2)


def main():
    passes = {calc_id(line) for line in stream_lines(day=5)}
    print(m := max(passes))
    print(max(set(range(m)) - passes))


if __name__ == '__main__':
    main()
