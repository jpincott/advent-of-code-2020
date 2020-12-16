from math import prod
from re import findall

from parse import parse

from aoc_2020.utils.decorators import timer


@timer
def get_input():
    with open('../input/day_16.txt') as f:
        rules, ticket, neigbbours = f.read().split('\n\n')
        return rules, ticket, neigbbours


@timer
def main():
    rules, ticket, neighbours = get_input()
    pt1(neighbours, rules)

    rules = {
        name: [range(x1, y1 + 1), range(x2, y2 + 1)]
        for r in rules.split('\n')
        for name, x1, y1, x2, y2 in [(parse('{}: {:d}-{:d} or {:d}-{:d}', r).fixed)]
    }

    neighbours = [
        [int(n) for n in l.split(',')]
        for l in neighbours.split('\n')[1:]
    ]

    # only valid neighbours
    neighbours = [
        n
        for n in neighbours
        if all([
            any([
                i in r for ranges in rules.values() for r in ranges
            ])
            for i in n
        ])
    ]

    # valid rules by position
    valid_rules = {}
    for f in range(len(rules)):
        is_possible = set()
        vals_to_test = [n[f] for n in neighbours]
        for rule, ranges in rules.items():
            rule_is_valid = True
            for val in vals_to_test:
                if all(val not in r for r in ranges):
                    rule_is_valid = False
            if rule_is_valid:
                is_possible.add(rule)
        valid_rules[f] = is_possible

    fixed = {}
    while valid_rules:
        to_remove = [(p, list(r)[0]) for p, r in valid_rules.items() if len(r) == 1]
        for p, r in to_remove:
            fixed[p] = r
            del valid_rules[p]
            for s in valid_rules.values():
                s.remove(r)

    fields = [i for i, r in fixed.items() if r.startswith('departure')]
    ticket = [int(n) for n in ticket.split('\n')[1].split(',')]

    print(prod(ticket[i] for i in fields))


def pt1(neighbours, rules):
    rules = [range(int(x), int(y) + 1) for x, y in findall(r'(\d+)-(\d+)', rules)]
    neighbours = [int(n) for n in findall(r'(\d+)', neighbours)]
    print(sum(n for n in neighbours if all(n not in r for r in rules)))


if __name__ == '__main__':
    main()
