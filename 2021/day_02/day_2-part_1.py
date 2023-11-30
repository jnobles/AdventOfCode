position = 0
depth = 0

with open('day_2-input') as f:
    for line in f.readlines():
        instruction, value = line.split()
        if instruction == 'forward':
            position += int(value)
        elif instruction == 'down':
            depth += int(value)
        elif instruction == 'up':
            depth -= int(value)
print(position * depth)
