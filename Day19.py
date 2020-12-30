from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n', ': | '])
#when copying the puzzle input into input.txt, remove the quotes around "a" and "b"

def check(text, rules, rnum):
    rule = next(r for r in rules if r[0] == rnum)
    pipe_index = rule.index('|') if '|' in rule else -1

    if rule[1] == 'a' or rule[1] == 'b':
        if text[0] == rule[1]: return text[1:]
        return None

    i = 1
    working_text = text
    while i < len(rule):
        if rule[i] == '|': return working_text
        working_text = check(working_text, rules, rule[i])
        if working_text == None:
            if pipe_index == -1 or i > pipe_index: return None
            else:
                i = pipe_index
                working_text = text
        i += 1
    return working_text

def part2_check(text, rules, step):
    ft, to = 0, 0
    for i in range (len(text) // step):
        result = check(text[i * step : (i + 1) * step], rules, 42)
        if result == '':
            if to != 0: return False
            ft += 1
        elif result == None: to += 1
    return ft > to and to > 0

count = 0
for text in data[1]:
    if check(text, data[0], 0) == '': count += 1
print(count)

count = 0
for text in data[1]:
    if part2_check(text, data[0], 8): count += 1
print(count)