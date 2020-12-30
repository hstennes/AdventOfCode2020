import numpy as np
from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n'])

def get_sides(tile):
    sides = [tile[:,-1], tile[0,:], tile[:,0], tile[-1,:]]
    values = []
    for side in sides:
        side_str = "".join(side).replace('#', '1').replace('.', '0')
        values.append((int(side_str, 2), int(side_str[::-1], 2)))
    return values

side_vals = {}
for tile in data: 
    sides = get_sides(np.array([list(row) for row in tile[1:]]))
    for s in sides:
        side = min(s)
        if side in side_vals: side_vals.pop(side)
        else: side_vals[side] = tile[0]
print(side_vals)
    
tiles = []
for side in side_vals:
    if side_vals[side] in tiles: print(side_vals[side])
    else: tiles.append(side_vals[side])
