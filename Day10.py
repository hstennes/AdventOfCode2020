from puzzle_input import read
data = read("input.txt", 0, ['\n'])
data.sort()

prev, ones, threes = 0, 0, 0
for val in data:
    if val - prev == 3: threes += 1
    else: ones += 1
    prev = val
threes += 1
print(ones * threes)

prev, streak, answer = 0, 0, 1
combinations = [0, 1, 1, 2, 4, 7]
for i in range(len(data)):
    last = i == len(data) - 1
    streak += 2 if last else 1
    
    if data[i] - prev != 1 or last:
        answer *= combinations[streak]
        streak = 0
    prev = data[i]

print(answer)