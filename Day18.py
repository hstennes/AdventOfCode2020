from puzzle_input import read
data = read("input.txt", 0, ['\n'])

def match_index(exp, index):
    find_close = exp[index] == '('
    paren_count, i = (1 if find_close else -1), index + (1 if find_close else -1)
    while True:
        if exp[i] == '(': paren_count += 1
        elif exp[i] == ')': paren_count -= 1
        if paren_count == 0: break
        i += 1 if find_close else -1
    return i

def evaluate(exp):
    i, answer, last_op = 0, 0, ''
    while i < len(exp):
        jump = 0
        if exp[i] == '+' or exp[i] == '*': last_op = exp[i]
        else:
            val = 0
            if exp[i].isdigit(): val = int(exp[i])
            else:
                jump = match_index(exp, i)
                val = evaluate(exp[i + 1: jump])
            if i == 0: answer = val
            elif last_op == '+': answer += val
            else: answer *= val
        i = i + 1 if jump == 0 else jump + 1
    return answer

def parenthisize(exp):
    for i in range(exp.count('+')):
        count = 0
        for c in range(len(exp)):
            if exp[c] == '+': count += 1
            if count == i + 1:
                lower = c - 1 if exp[c - 1].isdigit() else match_index(exp, c - 1)
                upper = c + 1 if exp[c + 1].isdigit() else match_index(exp, c + 1)
                exp = exp[:lower] + '(' + exp[lower:upper + 1] + ')' + exp[upper + 1:]
                break
    return exp

part1 = 0
for line in data:
    part1 += evaluate(parenthisize(line.replace(' ', '')))
print(part1)