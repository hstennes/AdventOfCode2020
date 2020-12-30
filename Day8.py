from puzzle_input import read
data = read("input.txt", 0, ['\n', ' '])

def run(program):
    used_list = []
    acc = 0
    index = 0
    while True:
        if index in used_list:
            #print(acc)
            return False
        if index >= len(program): 
            print(acc)
            return True
        used_list.append(index)
        instruction = program[index]
        if instruction[0] == 'acc': 
            acc += instruction[1]
            index += 1
        elif instruction[0] == 'jmp': index += instruction[1]
        elif instruction[0] == 'nop': index += 1

run(data)

for line in data:
    if line[0] == 'jmp':
        line[0] = 'nop'
        if run(data): break
        line[0] = 'jmp'
    if line[0] == 'nop':
        line[0] = 'jmp'
        if run(data): break
        line[0] = 'nop'