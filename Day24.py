from puzzle_input import read
import copy
data = read('input.txt', 0, ['\n'])

tiles = {}
for line in data:
    x, y = 0, 0
    while len(line) > 0:
        east_or_west = False
        if line[0] == 'e': 
            x += 1
            east_or_west = True
        elif line[0] == 'w': 
            x -= 1
            east_or_west = True
        elif line[:2] == 'se':
            y += 1
            x += 1 if y % 2 == 0 else 0
        elif line[:2] == 'sw':
            y += 1
            x += 0 if y % 2 == 0 else -1
        elif line[:2] == 'ne':
            y -= 1
            x += 1 if y % 2 == 0 else 0
        elif line[:2] == 'nw':
            y -= 1
            x += 0 if y % 2 == 0 else -1
        if east_or_west: line = line[1:]
        else: line = line[2:]

    if (x, y) in tiles: tiles[(x, y)] = not(tiles[(x, y)])
    else: tiles[(x, y)] = True

count = 0
for key in tiles:
    if tiles[key]: count += 1
print(count)

offsets = [(-1, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
def count_surrounding(position, tiles):
    return sum(coord in tiles and tiles[coord] == True for coord in list_surrounding(position))

def list_surrounding(position):
    return [(position[0] + (offset[0] if position[1] % 2 == 1 else -offset[0]), position[1] + offset[1]) for offset in offsets]

for i in range(100):
    new_tiles = copy.deepcopy(tiles)
    for key in tiles:
        if tiles[key] == True:
            count = count_surrounding(key, tiles)
            if count == 0 or count > 2: new_tiles[key] = False
            for coord in list_surrounding(key):
                if not(coord in tiles) or tiles[coord] == False:
                    count = count_surrounding(coord, tiles)
                    if count == 2: new_tiles[coord] = True
    tiles = new_tiles

count = 0
for key in tiles:
    if tiles[key]: count += 1
print(count)