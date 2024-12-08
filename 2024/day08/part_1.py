with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

field_size = (len(puzzle_input[0]), len(puzzle_input))
antenna_locations = dict()

for y, row in enumerate(puzzle_input):
    for x, item in enumerate(row):
        if item == ".":
            continue
        known_locations = antenna_locations.get(item, [])
        known_locations.append([x, y])
        antenna_locations[item] = known_locations

print(antenna_locations)

antinode_locations = set()

for frequency in antenna_locations:
    for i, [antenna_x, antenna_y] in enumerate(antenna_locations[frequency]):
        other_antennas = antenna_locations[frequency][:i] + antenna_locations[frequency][i+1:]
        for other_antenna_x, other_antenna_y in other_antennas:
            x_distance = other_antenna_x - antenna_x
            y_distance = other_antenna_y - antenna_y
            antinode_x = antenna_x + 2 * x_distance
            antinode_y = antenna_y + 2 * y_distance
            if 0 <= antinode_x <= field_size[0] - 1 and 0 <= antinode_y <= field_size[1] - 1:
                antinode_locations.add((antinode_x, antinode_y))
print(len(antinode_locations), antinode_locations)
