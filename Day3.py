from puzzle_input import read
data = read("input.txt", 0, ['\n'])

def count_trees(data, step):
    rl = len(data[0])
    answer = 0
    for i in range(len(data)):
        x = float(i * step)
        if x.is_integer() and data[i][int(x % rl)] == '#': answer += 1
    return answer

print(count_trees(data, 1) * count_trees(data, 3) * count_trees(data, 5) * count_trees(data, 7) * count_trees(data, 0.5))