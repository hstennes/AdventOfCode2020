from puzzle_input import read
data = read("input.txt", ["\n", "-|: | "])

part1 = 0
for row in data:
    count = row[3].count(row[2])
    if count >= row[0] and count <= row[1]: part1 += 1

part2 = 0
for row in data:
    c = row[2]
    if (row[3][row[0] - 1] == c) ^ (row[3][row[1] - 1] == c): part2 += 1

print(part1)
print(part2)