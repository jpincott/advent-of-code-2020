from itertools import count

from aoc_2020.utils.io import stream_lines


def get_private_key(pub):
    v = 1
    for n in count(1):
        v *= 7
        v %= 20201227
        if pub == v:
            return n


def get_encryption_key(pub, priv):
    return pow(pub, priv, 20201227)


def main():
    pub_c, pub_d = [int(n) for n in stream_lines(day=25)]
    print(get_encryption_key(pub_d, get_private_key(pub_c)))
    print(get_encryption_key(pub_c, get_private_key(pub_d)))


if __name__ == '__main__':
    main()
