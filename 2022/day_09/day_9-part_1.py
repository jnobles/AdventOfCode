import math

with open('day_9-input') as f:
    steps = [line.rstrip() for line in f.readlines()]

for item, step in enumerate(steps):
    direction, distance = step.split()[0], int(step.split()[1])
    if direction == 'R':
        instruction = ('x', distance)
    elif direction == 'L':
        instruction = ('-x', distance)
    elif direction == 'U':
        instruction = ('y', distance)
    elif direction == 'D':
        instruction = ('-y', distance)
    steps[item] = instruction

max_x, max_y = 0, 0
min_x, min_y = 0, 0
curr_x, curr_y = 0, 0
for axis, distance in steps:
    if axis == 'x':
        curr_x += distance
    elif axis == '-x':
        curr_x -= distance
    elif axis == 'y':
        curr_y += distance
    elif axis == '-y':
        curr_y -= distance
    max_x, max_y = max(curr_x, max_x), max(curr_y, max_y)
    min_x, min_y = min(curr_x, min_x), min(curr_y, min_y)
grid = [['.' for i in range(min_x, max_x+1)] for j in range(min_y, max_y+1)]

head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
grid[tail_y][tail_x] = '#'

def get_distance(a, b, x, y):
    return math.sqrt(math.pow(a - x, 2) + math.pow(b - y, 2))

for axis, distance in steps:
    while distance > 0:
        if axis == 'x':
            head_x += 1
        elif axis == '-x':
            head_x -= 1
        elif axis == 'y':
            head_y += 1
        elif axis == '-y':
            head_y -= 1

        if get_distance(head_x, head_y, tail_x, tail_y) > 1.5:
            if head_x == tail_x:
                if axis == 'x':
                    tail_y += 1
                elif axis == '-x':
                    tail_y -= 1
                elif axis == 'y':
                    tail_y += 1
                elif axis == '-y':
                    tail_y -= 1
            elif head_y == tail_y:
                if axis == 'x':
                    tail_x += 1
                elif axis == '-x':
                    tail_x -= 1
                elif axis == 'y':
                    tail_x += 1
                elif axis == '-y':
                    tail_x -= 1
            else:
                if head_x > tail_x and head_y > tail_y:
                    tail_x += 1
                    tail_y += 1
                elif head_x < tail_x and head_y > tail_y:
                    tail_x -= 1
                    tail_y += 1
                elif head_x > tail_x and head_y < tail_y:
                    tail_x += 1
                    tail_y -= 1
                elif head_x < tail_x and head_y < tail_y:
                    tail_x -= 1
                    tail_y -= 1
        grid[tail_y][tail_x] = '#'
        distance -= 1

count = 0
for row in grid:
    for item in row:
        if item == '#':
            count += 1
print(count)