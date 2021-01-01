from puzzle_input import read
data = read('input.txt', 0, ['\n', r'\(', ' |, '])

algn_dict = {}
for line in data:
  for allergen in line[1][1:]:
      allergen = allergen.removesuffix(')')
      if allergen in algn_dict: algn_dict[allergen] = list(set(algn_dict[allergen]) & set(line[0]))
      else: algn_dict[allergen] = line[0]

count = 0
for line in data:
  for igrd in line[0]:
    if not any(igrd in algn_dict[key] for key in algn_dict): count += 1
print(count)

while True:
  allergen = next(a for a in algn_dict if type(algn_dict[a]) != str and len(algn_dict[a]) == 1)
  algn_dict[allergen] = only = algn_dict[allergen][0]

  done = True
  for allergen in algn_dict:
    igrd_list = algn_dict[allergen]
    if type(igrd_list) != str:
      done = False
      if only in igrd_list: igrd_list.remove(only)
  if done: break

print(','.join([algn_dict[key] for key in sorted(list(algn_dict.keys()))]))