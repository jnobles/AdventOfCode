position = 0
depth = 0
aim = 0

with open('day_2-input') as f:
    for line in f.readlines():
        instruction, value = line.split()
        if instruction == 'forward':
            position += int(value)
            depth += int(value) * aim
        elif instruction == 'down':
            aim += int(value)
        elif instruction == 'up':
            aim -= int(value)
print(position * depth)
