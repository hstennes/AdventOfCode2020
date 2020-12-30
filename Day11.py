import copy
from puzzle_input import read

rawdata = read("input.txt", 0, ['\n'])
data = [[char for char in row] for row in rawdata]
directions = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))

def count_adj(data, r, c):
    count = 0
    for direction in directions:
        row = r + direction[0]
        col = c + direction[1]
        if 0 <= row < len(data) and 0 <= col < len(data[0]):
            if data[row][col] == '#': count += 1
    return count

def count_see(data, r, c):
    count = 0
    for direction in directions:
        row, col = r, c
        while True:
            row += direction[0]
            col += direction[1]
            if 0 <= row < len(data) and 0 <= col < len(data[0]):
                if data[row][col] == '#': 
                    count += 1
                    break
                elif data[row][col] == 'L': break
            else: break
    return count

while True:
    change = False
    newdata = copy.deepcopy(data)
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == '#' and count_see(data, r, c) >= 5: 
                newdata[r][c] = 'L'
                change = True
            elif data[r][c] == 'L' and count_see(data, r, c) == 0: 
                newdata[r][c] = '#'
                change = True
    data = newdata
    if not change: break

answer = 0
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '#': answer += 1

print(answer)