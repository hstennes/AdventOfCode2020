from puzzle_input import read
data = read("input.txt", 0, ['\n'])

part1 = 0
for i in range(len(data)):
    if i > 24:
        found = False
        for a in data[i - 25:i]:
            for b in data[i - 25:i]:
                if a + b == data[i]:
                    found = True
        if not found: 
            print(data[i])
            part1 = data[i]
            break

for i in range(len(data)):
    sum = 0
    for x in range(i, len(data)):
        sum += data[x]
        if sum == part1:
            print(max(data[i:x + 1]) + min(data[i:x + 1]))
        elif sum > part1:
            break