import numpy as np
from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n'])

#right, top, left, bottom
def get_sides(tile):
    sides = [tile[:,-1], tile[0,:], tile[:,0][::-1], tile[-1,:][::-1]]
    values = []
    for side in sides:
        side_str = "".join(side).replace('#', '1').replace('.', '0')
        values.append((int(side_str, 2), int(side_str[::-1], 2)))
    return values

side_to_edge_tile = {}
for tile in data: 
    sides = get_sides(np.array([list(row) for row in tile[1:]]))

    #if '3847' in tile[0] or '3919' in tile[0]: print(sides)

    for s in sides:
        side = min(s)
        if side in side_to_edge_tile: side_to_edge_tile.pop(side)
        else: side_to_edge_tile[side] = tile[0]

for thing in side_to_edge_tile: print(thing, side_to_edge_tile[thing])
    
edge_tile_to_sides = {}
corners = []
for side in side_to_edge_tile:
    tile = side_to_edge_tile[side]
    if tile in edge_tile_to_sides: 
        print(tile, edge_tile_to_sides[tile], side)
        corners.append(int(tile.split(' ')[1][:-1]))
    else: edge_tile_to_sides[tile] = side

print(corners[0] * corners[1] * corners[2] * corners[3])