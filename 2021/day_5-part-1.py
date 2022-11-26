pairs = []

with open('day_5-input-practice') as f:
    for line in f.readlines():
        pair = []
        for vent_line in [x for x in line.rstrip().split(' -> ')]:
            pair.append(tuple([int(x) for x in vent_line.split(',')]))
        pairs.append(pair)

max_x = max_y = 0
for line in pairs:
    for pair in line:
        x, y = pair
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y

field = [[0 for i in range(max_x+1)] for j in range(max_y+1)]

for pair in pairs:
    start_x, start_y = pair[0]
    end_x, end_y = pair[1]

    if start_x == end_x:
        vent_line = []
        for y in range(min([start_y,end_y]), max([start_y,end_y])+1):
            vent_line.append((start_x,y))
        for x, y in vent_line:
            field[y][x] += 1
    elif start_y == end_y:
        vent_line = []
        for x in range(min([start_x,end_x]), max([start_x,end_x])+1):
            vent_line.append((x,start_y))
        for x, y in vent_line:
            field[y][x] += 1

intersections = 0
for row in field:
    for item in row:
        if item > 1:
            intersections += 1
print(intersections)

for row in field:
    for item in row:
        if item > 0:
            print(item, end='')
        else:
            print('.', end='')
    print()
