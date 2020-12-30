from puzzle_input import read
data = read("input.txt", 0, ["\n", ":", " ", "-"])

part1 = 0
for row in data:
    count = row[1].count(row[0][1])
    if count >= row[0][0][0] and count <= row[0][0][1]: part1 += 1

part2 = 0
for row in data:
    c = row[0][1]
    if (row[1][row[0][0][0] - 1] == c) ^ (row[1][row[0][0][1] - 1] == c): part2 += 1

print(part1)
print(part2)