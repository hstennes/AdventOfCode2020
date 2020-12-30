from puzzle_input import read
data = read("input.txt", 0, ['\n\n'])

total = 0
for group in data:
    string = group.replace('\n', '')
    temp=[]
    for i in string:
        if(i not in temp):
            temp.append(i)
    total += len(temp)

part2 = 0
for group in data:
    people = group.split('\n')
    num_in_all = 0
    for x in people[0]:
        in_all = True
        for person in people:
            if not(x in person): in_all = False
        if in_all: num_in_all += 1
    part2 += num_in_all

print(total)
print(part2)