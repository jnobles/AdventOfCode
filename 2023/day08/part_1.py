import re

with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

directions = [direction for direction in puzzle_input[0]]
nodes = {}
for line in puzzle_input[2:]:
    tmp = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
    nodes[tmp.group(1)] = (tmp.group(2), tmp.group(3))

current_node = 'AAA'
steps = 0
while current_node != 'ZZZ':
    direction = directions.pop(0)
    if direction == 'L':
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    directions.append(direction)
    steps += 1
    print(f'{current_node} ({steps})')
