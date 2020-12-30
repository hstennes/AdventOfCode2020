from puzzle_input import read
data = read("input.txt", 0, ['\n', 'contain|,'])

def get_color(bag_str):
    if bag_str == 'no other bags.': return 'no'
    without_suffix = bag_str.removesuffix('.').removesuffix('bag').removesuffix('bags').strip()
    return without_suffix[2:] if without_suffix[0].isdigit() else without_suffix

def get_number(bag_str):
    if bag_str == 'no other bags.': return 0
    return int(bag_str[:2])

def list_containers(data, color):
    containers = []
    for row in data:
        for bag in row[1:]:
            if get_color(bag) == color:
                row_color = get_color(row[0])
                new_list = list_containers(data, row_color)
                if not row_color in containers: containers.append(row_color)
                containers.extend([i for i in new_list if (not i in containers)])
    return containers

def list_contained(data, color):
    print(color)
    count = 0
    for row in data:
        row_color = get_color(row[0])
        if row_color == color:
            for bag in row[1:]:
                count += get_number(bag) * (list_contained(data, get_color(bag)) + 1)
    return count

print(len(list_containers(data, 'shiny gold')))
print(list_contained(data, 'shiny gold'))