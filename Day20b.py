import numpy as np
from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n'])
tsize, grid_size = 10, 12
image_size = (tsize - 2) * grid_size

def get_sides(tile):
    sides = [tile[:,-1], tile[0,:], tile[:,0], tile[-1,:]]
    values = []
    for side in sides:
        side_str = "".join(side).replace('#', '1').replace('.', '0')
        values.append((int(side_str, 2), int(side_str[::-1], 2)))
    return values

side_to_id, id_to_tile = {}, {}
for tile in data: 
    array = np.array([list(row) for row in tile[1:]])
    id_to_tile[int(tile[0].split(' ')[1].removesuffix(':'))] = array
    for s in get_sides(array): side_to_id[s[0]] = (id, s[1])

image = np.empty((image_size, image_size), dtype = str)

last_rstart = 0
for r in range(0, image_size, tsize - 2):
    if r == 0: last_tile = 3847
    else:

    for c in range(0, image_size, tsize - 2):

        image[r:r + tsize - 2, c:c + tsize - 2] = tile[1:tsize - 1, 1:tsize - 1]

print(image)