from puzzle_input import read
import copy
data = read("input.txt", 0, ['\n\n', '\n'])

def play(p1, p2):
    p1s, p2s, = [], []
    while len(p1) > 0 and len(p2) > 0:
        p1s.append(copy.deepcopy(p1))
        p2s.append(copy.deepcopy(p2))
        winner, loser = [], []
        if len(p1) >= p1[0] + 1 and len(p2) >= p2[0] + 1:
            winner, loser = (p1, p2) if play(p1[1: 1 + p1[0]], p2[1: 1 + p2[0]])[0] else (p2, p1)
        else: 
            winner, loser = (p1, p2) if p1[0] > p2[0] else (p2, p1)
        winner.append(winner.pop(0))
        winner.append(loser.pop(0))

        p1_repeat, p2_repeat = False, False
        for item in p1s:
            if item == p1:
                p1_repeat = True
                break
        for item in p2s:
            if item == p2:
                p2_repeat = True
                break
        if p1_repeat and p2_repeat: return (True, p1)
    return (True, p1) if len(p2) == 0 else (False, p2)

p1, p2 = data[0][1:], data[1][1:]
part2 = 0
winner = play(p1, p2)[1]
for i in range(len(winner)):
    part2 += winner[i] * (len(winner) - i)

print(part2)