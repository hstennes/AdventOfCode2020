from puzzle_input import read
data = read("input.txt", 0, ['\n', ','])
notes = data[1]

time = int(data[0])
min_wait = time
min_bus = -1
for bus in notes:
    if bus != 'x':
        wait = (time // bus + 1) * bus - time
        if wait < min_wait:
            min_wait = wait
            min_bus = bus
print(min_bus * min_wait)

def find_first(a, b, offset):
    t = 0
    while True:
        if (a * t + offset) % b == 0: return t * a
        t += 1

lcm, last = 1, 0
for i in range(len(notes)):
    if notes[i] != 'x':
        if i != 0: last += find_first(lcm, notes[i], last + i)
        lcm *= notes[i]
print(last)