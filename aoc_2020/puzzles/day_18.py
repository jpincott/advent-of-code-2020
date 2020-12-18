import operator
import re
from collections import deque

from aoc_2020.utils.io import stream_lines


def get_tokens():
    return (deque(re.findall(r'(\d+|\S)', l)) for l in stream_lines(day=18))


def term(t, tokens):
    if t.isnumeric():
        return int(t)
    if t == '(':
        return evaluate(tokens)
    return 't'


def evaluate(tokens):
    l = term(tokens.popleft(), tokens)
    while(tokens):
        o = tokens.popleft()
        if o == ')': break
        r = term(tokens.popleft(), tokens)
        l = {'+': operator.add, '*': operator.mul}[o](l, r)
    return l


def main():

    print(sum(map(evaluate, get_tokens())))



if __name__ == '__main__':
    main()
