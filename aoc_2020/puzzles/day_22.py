from collections import deque
from itertools import islice
from math import prod

from aoc_2020.utils.decorators import timer


def get_decks():
    with open('../input/day_22.txt') as f:
        return [[int(n) for n in p.splitlines()[1:]] for p in f.read().split('\n\n')]


@timer
def main():
    p1, p2 = get_decks()
    print(f"Winning score: {abs(play_combat(p1, p2))}")
    print(f"Winning score: {abs(play_recursive_combat(p1, p2))}")


def score(cards):
    return sum(map(prod, enumerate(reversed(cards), start=1)))


def play_combat(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        p1.extend((c1, c2)) if c1 > c2 else p2.extend((c2, c1))
    return score(p1) - score(p2)


def play_recursive_combat(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    seen = set()
    while p1 and p2:
        if (key := (tuple(p1), tuple(p2))) in seen:
            return 0
        else:
            seen.add(key)

        c1, c2 = p1.popleft(), p2.popleft()
        if len(p1) < c1 or len(p2) < c2:
            p1.extend((c1, c2)) if c1 > c2 else p2.extend((c2, c1))
        else:
            s = play_recursive_combat(islice(p1, 0, c1), islice(p2, 0, c2))
            p1.extend((c1, c2)) if s >= 0 else p2.extend((c2, c1))

    return score(p1) - score(p2)


if __name__ == '__main__':
    main()
