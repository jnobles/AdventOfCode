with open('day_9-input-practice') as f:
    steps = [line.rstrip() for line in f.readlines()]

for item, step in enumerate(steps):
    direction, distance = step.split()[0], int(step.split()[1])
    if direction == 'L':
        instruction = ('x', -distance)
    elif direction == 'R':
        instruction = ('x', distance)
    elif direction == 'U':
        instruction = ('y', distance)
    elif direction == 'D':
        instruction = ('y', distance)
    steps[item] = instruction

max_x, max_y = 0, 0
curr_x, curr_y = 0, 0
for axis, distance in steps:
    if axis == 'x':
        curr_x += distance
    elif axis == 'y':
        curr_y += distance
    max_x, max_y = max(curr_x, max_x), max(curr_y, max_y)
grid = [['.' for i in range(max_x+1)] for j in range(max_y+1)]

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
grid[tail_y][tail_x] = '#'

for axis, distance in steps:
    while distance != 0:
        if axis == 'x':
            head_x += 1
        elif axis == 'y':
            head_y += 1

        if head_x == tail_x and head_y == tail_y:
            pass
        elif head_x == tail_x and head_y == tail_y - 1:
            tail_y += 1

        distance -= 1