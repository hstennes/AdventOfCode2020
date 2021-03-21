import numpy as np
import re
from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n'])
tsize, grid_size = 10, 12
starter_tile = '3847'
image_size = (tsize - 2) * grid_size

#each tile as a tuple with index 0 containing ID line and index 1 containing np array
tiles = [(tile[0], np.array([list(row) for row in tile[1:]])) for tile in data]

#right, top, left, bottom
def get_sides(tile):
    sides = [tile[:,-1], tile[0,:], tile[:,0][::-1], tile[-1,:][::-1]]
    values = []
    for side in sides:
        side_str = "".join(side).replace('#', '1').replace('.', '0')
        values.append((int(side_str, 2), int(side_str[::-1], 2)))
    return values

#returns tuple with trimmed tile, right side, and bottom side
def tile_info_by_id(id):
    for tile in tiles:
        if id in tile[0]:
            sides = get_sides(tile[1])
            tiles.remove(tile)
            return (tile[1][1:-1,1:-1], sides[0], sides[3])

def get_connecting_tile(connect_side, connect_direction, tiles):
    for tile in tiles:
        sides = get_sides(tile[1])
        for direction in range(len(sides)):
            current_side = sides[direction]
            if min(current_side) == min(connect_side):
                tiles.remove(tile)
                final_tile = np.rot90(tile[1], (connect_direction - direction) % 4).copy()
                if current_side[1] == connect_side[1]:
                    if connect_direction % 2 == 0: final_tile = np.flipud(final_tile).copy()
                    else: final_tile = np.fliplr(final_tile).copy()
                sides = get_sides(final_tile)
                return (final_tile[1:-1,1:-1], sides[0], sides[3])

def check_str(string, indexes):
    for index in indexes:
        if string[index] != '#': return False
    return True

image = np.empty((image_size, image_size), dtype = str)
row_connector = -1
for r in range(0, image_size, tsize - 2):

    column_connector, tile_info = -1, None
    if row_connector == -1: tile_info = tile_info_by_id(starter_tile)
    else: tile_info = get_connecting_tile(row_connector, 1, tiles)
    image[r:r+tsize-2, 0:tsize-2] = tile_info[0]
    row_connector = tile_info[2]
    column_connector = tile_info[1]

    for c in range(tsize - 2, image_size, tsize - 2):
        tile_info = get_connecting_tile(column_connector, 2, tiles)
        image[r:r + tsize - 2, c:c + tsize - 2] = tile_info[0]
        column_connector = tile_info[1]

for row in image:
    print(''.join(row))

def find_monsters(image):
    count = 0
    for l in range(1, len(image) - 1):
        line = ''.join(image[l])
        matches = re.finditer(r'#.{4}#{2}.{4}#{2}.{4}#{3}', line)
        for match in matches:
            if re.match(r'#.{2}#.{2}#.{2}#.{2}#.{2}#', ''.join(image[l + 1])[match.start() + 1:match.end() - 3]) and ''.join(image[l - 1])[match.end() - 2] == '#':
                print("munster at", l, match.start())
                count += 1
    return count

def count_hashtags(image):
    count = 0
    for row in image: count += ''.join(row).count('#')
    return count

hashtag_count = count_hashtags(image)
for direction in range(4):
    count = find_monsters(np.rot90(image, direction).copy())
    if count != 0: 
        print(hashtag_count - 15 * count)
        break
    count = rot_flip_image = find_monsters(np.rot90(np.fliplr(image), direction).copy())
    if count != 0:
        print(hashtag_count - 15 * count)
        break

'''program outputs 2161, but the answer is 2146 as determined by a lucky guess.  There is one mysterious monster that the program does not detect.'''