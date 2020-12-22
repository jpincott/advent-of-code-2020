from collections import deque


def get_decks():
    with open('../input/day_22.txt') as f:
        return [[int(n) for n in p.splitlines()[1:]] for p in f.read().split('\n\n')]


def main():
    p1, p2 = get_decks()

    # Pt 1
    r1, r2 = play_combat(p1, p2)
    print(f"P1: {score(r1)}, P2: {score(r2)}")

    # p2
    r1, r2, _ = play_recursive_combat(p1, p2)
    print(f"P1: {score(r1)}, P2: {score(r2)}")


def play_recursive_combat(p1, p2, g=1, r=1):
    p1, p2 = deque(p1), deque(p2)
    seen = set()
    while p1 and p2:
        key = f"{p1}:{p2}"
        if key in seen:
            # p1 wins game
            return p1, p2, True
        else:
            seen.add(key)

        # print()
        # print(f"-- R {r} (G {g}) --")
        # print(p1)
        # print(p2)
        c1, c2 = p1.popleft(), p2.popleft()
        # print(c1)
        # print(c2)
        if len(p1) < c1 or len(p2) < c2:
            # a normal round
            if c1 > c2:
                # print("P1")
                p1.append(c1)
                p1.append(c2)
            else:
                # print("P2")
                p2.append(c2)
                p2.append(c1)
        else:
            r1, r2, p1_win = play_recursive_combat(list(p1)[:c1], list(p2)[:c2], g+1)
            if p1_win or r1:
                # print("P1")
                p1.append(c1)
                p1.append(c2)
            else:
                # print("P2")
                p2.append(c2)
                p2.append(c1)
        r += 1

    return p1, p2, False


def score(cards):
    return sum(c + c * i for i, c in enumerate(reversed(cards)))


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
