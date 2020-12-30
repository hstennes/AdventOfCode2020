from puzzle_input import read
data = read("input.txt", 0, ['\n\n', '\n', ':|-| or |,'])
tickets = []
part1 = 0
for ticket in data[2][1:]:
    valid = True
    for n in ticket:
        if not any(f[1] <= n <= f[2] or f[3] <= n <= f[4] for f in data[0]): 
            part1 += n
            valid = False
            break
    if valid: tickets.append(ticket)
print(part1)

map = {}
for i in range(len(data[2][1])):
    for f in data[0]:
        valid = True
        for ticket in tickets:
            if not(f[1] <= ticket[i] <= f[2] or f[3] <= ticket[i] <= f[4]):
                valid = False
                break
        if valid:
            if f[0] in map: map[f[0]].append(i)
            else: map[f[0]] = [i]

print(map)
for _ in range(len(map)):
    for fieldA in map:
        if len(map[fieldA]) == 1:
            for fieldB in map:
                if len(map[fieldB]) != 1:
                    for i in range(len(map[fieldB])):
                        if map[fieldB][i] == map[fieldA][0]: 
                            map[fieldB].pop(i)
                            break

names = ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time']
part2 = 1
for name in names: part2 *= data[1][1][map[name][0]]
print(part2)