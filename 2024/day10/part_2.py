import copy

with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

topographical_map = [[int(val) for val in line] for line in puzzle_input]
trailhead_coords = []
target_coords = []
for y, row in enumerate(topographical_map):
    for x, height in enumerate(row):
        if height == 0:
            trailhead_coords.append([x, y])
        elif height == 9:
            target_coords.append([x, y])

map_height = len(topographical_map)
map_width = len(topographical_map[0])


def get_possible_directions(topographical_map, current_x, current_y, current_height):
    possible_directions = []
    if 0 <= current_x - 1 < map_width:  # is left on the grid?
        if topographical_map[current_y][current_x - 1] == current_height + 1:  # is left a valid step?
            possible_directions.append([current_x - 1, current_y])
    if 0 <= current_x + 1 < map_width:  # is right on the grid?
        if topographical_map[current_y][current_x + 1] == current_height + 1:  # is right a valid step?
            possible_directions.append([current_x + 1, current_y])
    if 0 <= current_y - 1 < map_height:  # is up on the grid?
        if topographical_map[current_y - 1][current_x] == current_height + 1:  # is up a valid step?
            possible_directions.append([current_x, current_y - 1])
    if 0 <= current_y + 1 < map_height:  # is down on the grid?
        if topographical_map[current_y + 1][current_x] == current_height + 1:  # is down a valid step?
            possible_directions.append([current_x, current_y + 1])
    return possible_directions


open_nodes = trailhead_coords
valid_node_count = 0
while open_nodes:
    node_x, node_y = open_nodes.pop()
    height = topographical_map[node_y][node_x]
    if height == 9:
        valid_node_count += 1
    else:
        new_nodes = get_possible_directions(topographical_map, node_x, node_y, height)
        open_nodes += new_nodes

print(valid_node_count)
