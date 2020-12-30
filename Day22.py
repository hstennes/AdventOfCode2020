from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n'])

p1, p2 = data[0][1:], data[1][1:]

while len(p1) > 0 and len(p2) > 0:
    if p1[0] > p2[0]:
        p1.append(p1.pop(0))
        p1.append(p2.pop(0))
    else:
        p2.append(p2.pop(0))
        p2.append(p1.pop(0))
    
winner = p1 if len(p2) == 0 else p2
part1 = 0
for i in range(len(winner)):
    part1 += winner[i] * (len(winner) - i)

print(part1)