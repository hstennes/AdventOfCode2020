import pprint
from puzzle_input import read
import copy
data = read("input.txt", 0, ['\n'])

iters = 6
dl, dr, dc = 2 * iters + 1, 2 * iters + len(data), 2 * iters + len(data[0])
world = [[['.' for c in range(dc)] for r in range(dr)] for l in range(dl)]
for r in range(len(data)):
    for c in range(len(data[0])):
        world[iters][r + iters][c + iters] = data[r][c]

def count_surrounding(world, l, r, c):
    count = 0
    for il in range(max(0, l - 1), min(dl - 1, l + 1) + 1):
        for ir in range(max(0, r - 1), min(dr - 1, r + 1) + 1):
            for ic in range(max(0, c - 1), min(dc - 1, c + 1) + 1):
                if il != l or ir != r or ic != c:
                    if world[il][ir][ic] == '#': count += 1
    return count

for i in range(6):
    new_world = copy.deepcopy(world)
    for l in range(dl):
        for r in range(dr):
            for c in range(dc):
                count = count_surrounding(world, l, r, c)
                if world[l][r][c] == '#':
                    if count != 2 and count != 3: new_world[l][r][c] = '.'
                else:
                    if count == 3: new_world[l][r][c] = '#'
    world = new_world

part1 = 0
for l in range(dl):
    for r in range(dr):
        for c in range(dc):
            if world[l][r][c] == '#': part1 += 1
print(part1)