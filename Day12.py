from puzzle_input import read
data = read("input.txt", 1, ['\n', 1])

x, y = 0, 0
direction = 0
for line in data:
    if line[0] == 'L': direction = (direction + (line[1] / 90)) % 4
    elif line[0] == 'R': direction = (direction - (line[1] / 90)) % 4
    elif line[0] == 'F':
        if direction == 0: x += line[1]
        elif direction == 1: y += line[1]
        elif direction == 2: x -= line[1]
        elif direction == 3: y -= line[1]
    elif line[0] == 'E': x += line[1]
    elif line[0] == 'N': y += line[1]
    elif line[0] == 'W': x -= line[1]
    elif line[0] == 'S': y -= line[1]
print(abs(x) + abs(y))

wx, wy = 10, 1
x, y = 0, 0
for line in data:
    if line[0] == 'F':
        x += wx * line[1]
        y += wy * line[1]
    elif line[0] == 'E': wx += line[1]
    elif line[0] == 'N': wy += line[1]
    elif line[0] == 'W': wx -= line[1]
    elif line[0] == 'S': wy -= line[1]
    else:
        angle = line[1]
        while angle > 0:
            temp = wx
            wx = wy
            wy = temp
            if line[0] == 'L': wx *= -1
            else: wy *= -1
            angle -= 90
print(abs(x) + abs(y))