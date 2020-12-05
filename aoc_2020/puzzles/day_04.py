from re import fullmatch, findall


def get_input():
    with open('../input/day_4.txt') as f:
        return [dict(findall(r'(\w{3}):(\S*)', c)) for c in f.read().split('\n\n')]


def has_required_fields(passport):
    reqd = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return reqd.issubset(passport.keys())


def is_valid(passport):
    if not has_required_fields(passport):
        return False
    if int(passport['byr']) not in range(1920, 2002 + 1):
        return False
    if int(passport['iyr']) not in range(2010, 2020 + 1):
        return False
    if int(passport['eyr']) not in range(2020, 2030 + 1):
        return False
    if not (m := fullmatch(r'(\d+)(cm|in)', passport['hgt'])):
        return False
    else:
        n, u = m.groups()
        if u == 'cm' and int(n) not in range(150, 193 + 1):
            return False
        if u == 'in' and int(n) not in range(59, 76 + 1):
            return False
    if not fullmatch('#[0-9a-f]{6}', passport['hcl']):
        return False
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not fullmatch(r'\d{9}', passport['pid']):
        return False
    return True


def main():
    passports = get_input()
    print(sum(has_required_fields(p) for p in passports))
    print(sum(is_valid(p) for p in passports))


if __name__ == '__main__':
    main()
