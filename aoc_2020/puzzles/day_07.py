from re import findall

from aoc_2020.utils.io import stream_lines


def get_rules():
    return {
        outer: {inner: int(count) for count, inner in findall(r'(\d+) (\w+ \w+)', contents)}
        for outer, contents in [line.split(' bags contain ') for line in stream_lines(day=7)]
    }


def can_contain_bag(rules, bag, outer):
    return bag in (inners := rules[outer]) or any(can_contain_bag(rules, bag, inner) for inner in inners)


def count_nested_bags(rules, colour):
    return sum(count * (1 + count_nested_bags(rules, inner)) for inner, count in rules[colour].items())


def main():
    rules = get_rules()
    print(sum(can_contain_bag(rules, 'shiny gold', bag) for bag in rules.keys()))
    print(count_nested_bags(rules, 'shiny gold'))


if __name__ == '__main__':
    main()
