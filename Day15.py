num_dict = {20: 1, 0: 2, 1: 3, 11: 4, 6: 5}

last = 3
for i in range(7, 30000001):
    if last in num_dict:
        temp = i - 1 - num_dict[last]
        num_dict[last] = i - 1
        last = temp
    else:
        num_dict[last] = i - 1 
        last = 0

print(last)