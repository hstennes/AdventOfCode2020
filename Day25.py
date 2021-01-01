from puzzle_input import read
data = read('input.txt', 0, ['\n'])

val = 1
i = 0
while True:
  i += 1
  val *= 7
  val %= 20201227
  if val == data[0]: break

val = 1
for x in range(i):
  val *= data[1]
  val %= 20201227

print(val)