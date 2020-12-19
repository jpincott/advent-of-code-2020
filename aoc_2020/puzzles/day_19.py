from regex import regex


def get_inputs():
    with open('../input/day_19.txt') as f:
        rules, messages = f.read().split('\n\n')
        return [r.split(': ') for r in rules.splitlines()], messages.splitlines()


class Rule():

    def __init__(self, key, pattern):
        self._key = key
        self._pattern = pattern.strip('"')

    def __repr__(self):
        return f"Key: '{self._key}', Pattern: '{self._pattern}'"

    def print(self, rules):
        # terminal case(s)
        if self._pattern in 'ab':
            return f'{self._pattern}'

        # recursive case
        s = "|".join(f'{"".join(self.format(rules, r) for r in grp.split(" "))}' for grp in self._pattern.split(' | '))
        return f'(?P<p{self._key}>{s})'

    def format(self, rules, r):
        if self._key != r:
            return rules[r].print(rules)
        else:
            return f'(?&p{self._key})'


def get_regex(rules):
    r = rules['0'].print(rules)
    return regex.compile(r)


def get_rules(rules):
    rules = {r[0]: Rule(*r) for r in rules}
    return rules


def main():
    rules, messages = get_inputs()

    # pt 1
    rules = get_rules(rules)
    re = get_regex(rules)
    print(sum(re.fullmatch(m) is not None for m in messages))

    # pt 2
    rules['8']._pattern = '42 | 42 8'
    rules['11']._pattern = '42 31 | 42 11 31'
    re = get_regex(rules)
    print(sum(re.fullmatch(m) is not None for m in messages))


if __name__ == '__main__':
    main()
