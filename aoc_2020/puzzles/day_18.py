import operator
import re
from collections import deque

from aoc_2020.utils.io import stream_lines


def get_tokens():
    return (deque(re.findall(r'(\d+|\S)', l)) for l in stream_lines(day=18))


def term(t, tokens, r):
    if t.isnumeric():
        return int(t)
    if t == '(':
        return evaluate(tokens, r)
    return 't'


def evaluate(tokens, fn):
    l = term(tokens.popleft(), tokens, fn)
    expr = deque([l])
    while (tokens):
        o = tokens.popleft()
        if o == ')': break
        r = term(tokens.popleft(), tokens, fn)
        expr.append(o)
        expr.append(r)

    return fn(expr)


def main():
    def lr(expr):
        l = expr.popleft()
        while expr:
            o = expr.popleft()
            r = expr.popleft()
            l = {'+': operator.add, '*': operator.mul}[o](l, r)
        return l

    print(sum(evaluate(t, lr) for t in get_tokens()))

    def am(expr):
        expr = list(expr)
        # add first
        while '+' in expr:
            i = expr.index('+')
            a = expr[:i - 1]
            b = expr[i - 1] + expr[i + 1]
            c = expr[i + 2:]
            expr = [*a, b, *c]

        # then multiply
        while '*' in expr:
            i = expr.index('*')
            a = expr[:i - 1]
            b = expr[i - 1] * expr[i + 1]
            c = expr[i + 2:]
            expr = [*a, b, *c]

        return expr[0]

    print(sum(evaluate(t, am) for t in get_tokens()))


if __name__ == '__main__':
    main()
