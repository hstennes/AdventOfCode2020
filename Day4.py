from puzzle_input import read
import re
data = read("input.txt", 0, ['\n\n', '\n| '])

def has_fields(passport):
    return len(passport) == 8 or (len(passport) == 7 and not("cid" in "".join(passport)))

def is_valid(passport):
    if not has_fields(passport): return False
    p = {i.split(':')[0]: i.split(':')[1] for i in passport}
    if not check_int(1920, 2002, p['byr']): return False
    if not check_int(2010, 2020, p['iyr']): return False
    if not check_int(2020, 2030, p['eyr']): return False
    if not (check_int(150, 193, p['hgt'].removesuffix('cm')) if 'cm' in p['hgt'] else check_int(59, 76, p['hgt'].removesuffix('in'))): return False
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', p['hcl']): return False
    if not p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    if not(is_int(p['pid']) and len(p['pid']) == 9): return False
    return True

def check_int(min, max, str):
    if not is_int(str): return False
    number = int(str)
    return number <= max and number >= min

def is_int(str):
    try:
        int(str)
        return True
    except ValueError: 
        return False

part1 = 0
part2 = 0
for passport in data:
    if has_fields(passport): part1 += 1
    if is_valid(passport): part2 += 1
print(part1, part2)

