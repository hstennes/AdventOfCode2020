from puzzle_input import read
data = read('input.txt', 0, [''])[1:-1]

'''data.extend(range(10, 50))'''

def pop_wrap(mylist, start, end):
    start %= len(mylist)
    end %= len(mylist)
    if end > start:
        removed = mylist[start:end]
        del mylist[start:end]
        return (end if start == 0 else 0, removed)
    else:
        removed = mylist[start:] + mylist[:end]
        del mylist[start:]
        del mylist[:end]
        return (end, removed)

current = 0
for i in range(10000000):
    d = data[current] - 1
    result = pop_wrap(data, current + 1, current + 4)
    current -= result[0]
    removed = result[1]
    destination = -1
    while d > 0:
        if d in data:
            destination = data.index(d)
            break
        d -= 1
    if destination == -1: destination = data.index(max(data))
    data[destination + 1: destination + 1] = removed
    current += 4 if destination < current else 1
    current %= len(data)
print(data)