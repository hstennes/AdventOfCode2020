from puzzle_input import read

input = read("input.txt", 0, "\n")
for x in input:
    for y in input:
        for z in input:
            if x + y + z == 2020:
                print(x * y * z)
