from puzzle_input import read
data = read("input.txt", 0, ['\n', 7])

max = 0
id_list = []
for item in data:
    row = int(item[0].replace('B', '1').replace('F', '0'), 2)
    column = int(item[1].replace('R', '1').replace('L', '0'), 2)
    id = row * 8 + column
    id_list.append(id)
    if id > max: max = id
print(max)

id_list.sort()
last_item = id_list[0]
for item in id_list:
    if item - last_item > 1: 
        print(item - 1)
        break
    last_item = item
