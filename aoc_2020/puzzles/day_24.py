import re
from collections import Counter

from aoc_2020.utils.io import stream_lines


def get_input():
    return [re.findall(r'(sw|se|nw|ne|w|e)', l) for l in stream_lines(day=24)]


def to_coords(steps):
    c = Counter(steps)
    ne, e, se = c['ne'] - c['sw'], c['e'] - c['w'], c['se'] - c['nw']
    return ne + e, se + e


def main():
    input = get_input()
    coords = [to_coords(steps) for steps in input]
    print(sum(v % 2 for v in Counter(coords).values()))


if __name__ == '__main__':
    main()
