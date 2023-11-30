heightmap = []
with open('day_9-input') as f:
    line = f.readline().rstrip()
    while line:
        temp = [int(line[i:i+1]) for i in range(len(line))]
        heightmap.append(temp)
        line = f.readline().rstrip()

low_points = []

for y in range(len(heightmap)):
    for x in range(len(heightmap[y])):
        vent_height = heightmap[y][x]
        is_low_spot = True
        adjacent_vents = [(x+1,y), (x, y+1), (x-1,y), (x,y-1)]
        for a, b in adjacent_vents:
            try:
                adjacent_height = heightmap[b][a]
            except IndexError:
                continue
            else:
                if not vent_height < adjacent_height:
                    is_low_spot = False
        if is_low_spot:
            risk_level = 1 + vent_height
            low_points.append([(x,y), risk_level])

print(sum([low_point[1] for low_point in low_points]))
