import re
from functools import reduce

from aoc_2020.utils.io import stream_lines


def get_recipes():
    return [
        (ings.split(' '), alls.split(', '))
        for matches in (re.findall(r'(.*) \(contains (.*)\)', l) for l in stream_lines(day=21))
        for ings, alls in matches
    ]


def get_candiate_ingredients_by_allergen(recipes):
    return reduce(
        lambda acc, t: acc | {t[0]: acc.get(t[0], t[1]) & t[1]},
        ((a, set(ings)) for ings, alls in recipes for a in alls),
        {}
    )


def resolve(todo, done):
    if not todo:
        return todo, done

    e = next((e for e in todo.items() if len(e[1]) == 1), None)
    if e is None:
        return todo, done

    return resolve(
        {k: v - e[1] for k, v in todo.items() if k != e[0]},
        done | {e[0]: e[1].pop()}
    )


def main():
    recipes = get_recipes()

    # map allergens to ingredients
    a_to_i = get_candiate_ingredients_by_allergen(recipes)

    _, allergens = resolve(a_to_i.copy(), {})
    print(allergens)

    # Pt1: all ingredients that can't be allergens
    s = sum(i not in allergens.values() for ings, _ in recipes for i in ings)
    print(s)

    # Pt2: stringy thingy
    s = ",".join(v for k, v in sorted(allergens.items()))
    print(s)


if __name__ == '__main__':
    main()
