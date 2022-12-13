import time
import os
os.system('')

class Cell:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    @staticmethod
    def calculate_h(point_a, point_b):
        a,b = point_a.x, point_a.y
        x,y = point_b.x, point_b.y
        return abs(a - x) + abs(b - y)

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x},{self.y})'

with open('day_12-input') as f:
    elevation_map = [line.rstrip() for line in f.readlines()]
    elevation_map = [[c for c in line] for line in elevation_map]

for y, line in enumerate(elevation_map):
    for x, c in enumerate(line):
        if c == 'S':
            start_x, start_y = x, y
            elevation_map[y][x] = 'a'
            break

for y, line in enumerate(elevation_map):
    for x, c in enumerate(line):
        if c == 'E':
            end_x, end_y = x, y
            elevation_map[y][x] = 'z'
            break

start_node = Cell(start_x, start_y, None)
end_node = Cell(end_x, end_y, None)

open_list = [start_node]
closed_list = []
report_interval = 100
report = report_interval
while len(open_list) > 0:
    if report == 0:
        report = report_interval
        for y in range(len(elevation_map)):
            for x in range(len(elevation_map[y])):
                temp = Cell(x, y, None)
                if temp == start_node:
                    print('S',end='')
                elif temp == end_node:
                    print('E',end='')
                elif temp in open_list:
                    print('O',end='')
                elif Cell(x, y, None) in closed_list:
                    print('X',end='')
                else:
                    print('.',end='')
            print()
        [print('\x1B[3A',end='') for i in range(len(elevation_map))]
    else:
        report -= 1
    open_list.sort(reverse=True)
    current_node = open_list.pop()
    closed_list.append(current_node)

    if current_node == end_node:
        path = []
        current = current_node
        while current is not None:
            path.append(current)
            current = current.parent
        print(len(path)-1)
        [print() for i in range(5)]
        for y in range(len(elevation_map)):
            for x in range(len(elevation_map[y])):
                if Cell(x, y, None) in path:
                    print('O',end='')
                elif Cell(x, y, None) in closed_list:
                    print('X',end='')
                else:
                    print('.',end='')
            print()
        break

    children = []
    for dx, dy in [(1,0), (0,1), (0,-1), (-1,0)]:
        if current_node.y + dy not in range(len(elevation_map)) \
        or current_node.x + dx not in range(len(elevation_map[0])):
            continue

        current_node_elevation = ord(elevation_map[current_node.y][current_node.x])
        target_node_elevation = ord(elevation_map[current_node.y + dy][current_node.x + dx])
        if target_node_elevation > current_node_elevation + 1:
            continue

        children.append(Cell(current_node.x + dx, current_node.y + dy, current_node))

    for child in children:
        is_valid = True
        if child in closed_list:
            continue

        if child in open_list:
            continue

        child.g = child.parent.g + 1
        child.h = Cell.calculate_h(child, end_node)
        child.f = child.g + child.h
        open_list.append(child)


#for y, line in enumerate(elevation_map):
#    for x, c in enumerate(line):
#        if c == 'S':
#            start_x, start_y = x, y
#            elevation_map[y][x] = 'a'
#            break
#
#elevations = 'abcdefghijklmnopqrstuvwxyzE'
#
#def take_step(x, y, elevation_map, steps):
#    if elevation_map[y][x] == 'E':
#        return 1
#
#    steps += 1
#    current_height = elevations.index(elevation_map[y][x])
#    new_map = [[item for item in line] for line in elevation_map]
#    new_map[y][x] = '.'
#
#    try:
#        if current_height + 1 >= elevations.index(new_map[y+1][x]):
#            steps = take_step(x, y+1, new_map, steps) + 1
#    except (IndexError, ValueError, TypeError):
#        pass
#
#    try:
#        if current_height + 1 >= elevations.index(new_map[y][x+1]):
#            steps = take_step(x+1, y, new_map, steps) + 1
#    except (IndexError, ValueError, TypeError):
#        pass
#
#    try:
#        if current_height + 1 >= elevations.index(new_map[y-1][x]):
#            steps = take_step(x, y-1, new_map, steps) + 1
#    except (IndexError, ValueError, TypeError):
#        pass
#
#    try:
#        if current_height + 1 >= elevations.index(new_map[y][x-1]):
#            steps = take_step(x-1, y, new_map, steps) + 1
#    except (IndexError, ValueError, TypeError):
#        pass
#
#    return steps
#
#print(take_step(start_x,start_y,elevation_map,0))
#
