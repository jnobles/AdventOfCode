class Node:
    def __init__(self, x, y, height, parent=None):
        self.x = x
        self.y = y
        self.height = ord(height)
        self.parent = parent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



with open('day_12-input') as f:
    elevation_map = [line.rstrip() for line in f.readlines()]
    elevation_map = [[c for c in line] for line in elevation_map]

for y, line in enumerate(elevation_map):
    for x, c in enumerate(line):
        if c == 'S':
            elevation_map[y][x] = 'a'
            break

for y, line in enumerate(elevation_map):
    for x, c in enumerate(line):
        if c == 'E':
            end_x, end_y = x, y
            elevation_map[y][x] = 'z'
            break

end_node = Node(end_x, end_y, 'z')

open_list = [end_node]
closed_list = []
while len(open_list) > 0:
    print(f'{len(open_list)} -- {len(closed_list)}')
    current_node = open_list.pop(0)
    closed_list.append(current_node)

    if current_node.height == ord('a'):
        steps = -1
        current = current_node
        while current is not None:
            steps += 1
            current = current.parent
        print(steps)
        break

    children = []
    for dx, dy in [(1,0), (0,1), (0,-1), (-1,0)]:
        if current_node.y + dy not in range(len(elevation_map)) \
        or current_node.x + dx not in range(len(elevation_map[0])):
            continue

        target_x = current_node.x + dx
        target_y = current_node.y + dy
        target_node = Node(target_x, target_y, elevation_map[target_y][target_x])
        if target_node.height + 1 < current_node.height:
            continue

        target_node.parent = current_node
        children.append(target_node)

    for child in children:
        if child in closed_list:
            continue

        if child in open_list:
            continue

        open_list.append(child)
