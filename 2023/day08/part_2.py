import math
import re

with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

nodes = {}
for line in puzzle_input[2:]:
    tmp = re.match(r'(.{3}) = \((.{3}), (.{3})\)', line)
    nodes[tmp.group(1)] = (tmp.group(2), tmp.group(3))

current_nodes = [node for node in nodes if node[-1] == 'A']
steps_to_z = [0 for node in current_nodes]

directions = [direction for direction in puzzle_input[0]]
for i, node in enumerate(current_nodes):
    while not current_nodes[i][-1] == 'Z':
        direction = directions.pop(0)
        if direction == 'L':
            current_nodes[i] = nodes[current_nodes[i]][0]
        else:
            current_nodes[i] = nodes[current_nodes[i]][1]
        directions.append(direction)
        steps_to_z[i] += 1
        print(f'{i} : {current_nodes[i]} {steps_to_z[i]}')
while len(steps_to_z) > 1:
    print(steps_to_z)
    a = steps_to_z.pop(0)
    b = steps_to_z.pop(0)
    lcm = int((a * b) / math.gcd(a, b))
    steps_to_z.append(lcm)
print(steps_to_z)
#steps = 0
#while not all([node[-1] == 'Z' for node in current_nodes]):
#    direction = directions.pop(0)
#    if direction == 'L':
#        for i, node in enumerate(current_nodes):
#            current_nodes[i] = nodes[current_nodes[i]][0]
#    else:
#        for i, node in enumerate(current_nodes):
#            current_nodes[i] = nodes[current_nodes[i]][1]
#    directions.append(direction)
#    steps += 1
#    print(f'{current_nodes} ({steps})')
