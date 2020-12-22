from collections import deque
from math import prod

from aoc_2020.utils.decorators import timer


def get_decks():
    with open('../input/day_22.txt') as f:
        return [[int(n) for n in p.splitlines()[1:]] for p in f.read().split('\n\n')]


@timer
def main():
    p1, p2 = get_decks()

    # Pt 1
    r1, r2 = play_combat(p1, p2)
    print(f"P1: {score(r1)}, P2: {score(r2)}")

    # p2
    r1, r2, _ = play_recursive_combat(p1, p2)
    print(f"P1: {score(r1)}, P2: {score(r2)}")


def play_recursive_combat(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    seen = set()
    while p1 and p2:
        key = (tuple(p1), tuple(p2))
        if key in seen:
            return p1, p2, True
        else:
            seen.add(key)

        c1, c2 = p1.popleft(), p2.popleft()
        if len(p1) < c1 or len(p2) < c2:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            r1, r2, p1_win = play_recursive_combat(list(p1)[:c1], list(p2)[:c2])
            if p1_win or r1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

    return p1, p2, False


def score(cards):
    return sum(map(prod, enumerate(reversed(cards), start=1)))


def play_combat(p1, p2):
    p1, p2 = deque(p1), deque(p2)
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return p1, p2


if __name__ == '__main__':
    main()
