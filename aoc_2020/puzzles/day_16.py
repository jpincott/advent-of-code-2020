from math import prod
from re import findall

from parse import findall

from aoc_2020.utils.decorators import timer


@timer
def main():
    rules, ticket, nearby = get_input()

    # pt 1
    invalid_tickets = find_invalid_tickets(rules, nearby)
    print(sum(nearby[i][j] for i, l in invalid_tickets.items() for j in l))

    # pt 2
    nearby = remove_invalid_tickets(invalid_tickets, nearby)
    fields = get_field_candidates(nearby, rules)
    fields = consolidate(fields, dict(), set())
    print(prod(ticket[i] for i, f in fields.items() if f.startswith('departure')))


def get_input():
    with open('../input/day_16.txt') as f:
        rules, ticket, nearby = f.read().split('\n\n')
        rules = {
            name: [range(x1, y1 + 1), range(x2, y2 + 1)]
            for r in rules.split('\n')
            for name, x1, y1, x2, y2 in findall('{}: {:d}-{:d} or {:d}-{:d}', r)
        }
        ticket = [int(n) for n in ticket.split('\n')[1].split(',')]
        nearby = [[int(n) for n in l.split(',')] for l in nearby.split('\n')[1:]]
        return rules, ticket, nearby


def find_invalid_tickets(rules, nearby):
    return {
        i: l
        for i, n in enumerate(nearby)
        if (l := [j for j, m in enumerate(n) if all(m not in r for ranges in rules.values() for r in ranges)])
    }


def remove_invalid_tickets(invalid_tickets, nearby):
    return [n for i, n in enumerate(nearby) if i not in invalid_tickets]


def get_field_candidates(nearby, rules):
    return {
        f: {r for r in rules if all(any(n in r for r in rules[r]) for n in [n[f] for n in nearby])}
        for f in range(len(rules))
    }


def consolidate(todo, done, used):
    return done if not todo else consolidate(
        {k: v for k, v in todo.items() if k != (f := min(todo, key=lambda k: len(todo[k] - used)))},
        done | {f: next(v for v in todo[f] - used)},
        used | todo[f]
    )


if __name__ == '__main__':
    main()
