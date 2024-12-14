with open("puzzle_input") as f:
    puzzle_input = f.read()

#grid_width, grid_height = 11, 7
grid_width, grid_height = 101, 103

import re

safety_factors = [] # safety factor, step
for steps in range(grid_width * grid_height):
    grid = [[0 for i in range(grid_width)] for j in range(grid_height)]
    for match in re.finditer(r"p=(?P<px>[-]?\d+),(?P<py>[-]?\d+) v=(?P<vx>[-]?\d+),(?P<vy>[-]?\d+)", puzzle_input):
        px = int(match.group("px"))
        py = int(match.group("py"))
        vx = int(match.group("vx"))
        vy = int(match.group("vy"))

        px += vx * steps
        py += vy * steps

        px %= grid_width
        py %= grid_height

        grid[py][px] += 1

    tlq = [grid[_][:grid_width // 2] for _ in range(grid_height // 2)]
    trq = [grid[_][grid_width // 2 + 1:] for _ in range(grid_height // 2)]
    blq = [grid[_][:grid_width // 2] for _ in range(grid_height // 2 + 1, grid_height)]
    brq = [grid[_][grid_width // 2 + 1:] for _ in range(grid_height // 2 + 1, grid_height)]

    safety_factor = 1
    for quad in [tlq, trq, blq, brq]:
        safety_factor *= sum([cell for row in quad for cell in row])

    safety_factors.append([safety_factor, steps])

safety_factors.sort()
print(safety_factors)
