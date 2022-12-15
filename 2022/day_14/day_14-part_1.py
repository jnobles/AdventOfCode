with open('day_14-input-practice') as f:
    rocks = [line.rstrip() for line in f.readlines()]
for i, rock in enumerate(rocks):
    rocks[i] = []
    for coords in rock.split(' -> '):
        x, y = coords.split(',')
        x = int(x)
        y = int(y)
        rocks[i].append([x,y])

max_x, max_y = 500, 0
min_x, min_y = 500, 0

for rock in rocks:
    for x,y in rock:
        max_x = max(int(x), max_x)
        min_x = min(int(x), min_x)
        max_y = max(int(y), max_y)
        min_y = min(int(y), min_y)

grid = [['░' for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]

for rock in rocks:
    for i in range(len(rock)-1):
        x_start = rock[i][0] - min_x
        y_start = rock[i][1] - min_y
        x_end = rock[i+1][0] - min_x
        y_end = rock[i+1][1] - min_y

        if x_start == x_end:
            for y in range(min(y_start, y_end), max((y_start, y_end))+1):
                grid[y][x_start] = '█'
        elif y_start == y_end:
            for x in range(min(x_start, x_end), max((x_start, x_end))+1):
                grid[y_start][x] = '█'

