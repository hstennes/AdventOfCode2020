import re
from puzzle_input import read
data = read("test.txt", 0, ['\n'])

def find_monsters(image):
    count = 0
    for l in range(1, len(image) - 1):
        line = image[l]
        matches = re.finditer(r'#.{4}#{2}.{4}#{2}.{4}#{3}', line)
        for match in matches:
            if re.match(r'#.{2}#.{2}#.{2}#.{2}#.{2}#', image[l + 1][match.start() + 1:match.end() - 3]) and image[l - 1][match.end() - 2] == '#':
                print("munster at", l, match.start())
                count += 1
    return count

def count_hashtags(image):
    count = 0
    for row in image: count += row.count('#')
    return count

if find_monsters(data) != 0:
    print(count_hashtags(data) - 15 * find_monsters(data))