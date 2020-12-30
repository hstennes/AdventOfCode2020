from puzzle_input import read
data = read("input.txt", 0, ['\n', '='])

def write_v1(memory, raw_address, raw_value, mask):
    address = raw_address[4 : len(line[0]) - 1]
    binary = bin(raw_value).replace('0b', '')
    binary = '0' * (36 - len(binary)) + binary

    value = ''
    for i in range(len(mask)):
        if mask[i] == 'X': value += binary[i]
        else: value += mask[i]

    memory[address] = int(value, base = 2)

def write_v2(memory, raw_address, raw_value, mask):
    addr_int = int(raw_address[4 : len(line[0]) - 1])
    binary = bin(addr_int).replace('0b', '')
    binary = '0' * (36 - len(binary)) + binary

    address = ''
    for i in range(len(mask)):
        if mask[i] == '0': address += binary[i]
        else: address += mask[i]

    floating_count = address.count('X')
    for i in range(2 ** floating_count):
        b = bin(i).replace('0b', '')
        b = '0' * (floating_count - len(b)) + b

        temp_address = ''
        counter = 0
        for c in range(len(address)):
            if address[c] == 'X': 
                temp_address += b[counter]
                counter += 1
            else: temp_address += address[c]

        memory[temp_address] = raw_value

mask = ''
memory = {}
for line in data:
    if line[0] == 'mask': mask = line[1]
    else: 
        write_v2(memory, line[0], line[1], mask)
        
sum = 0
for x in memory:
    sum += memory[x]
print(sum)