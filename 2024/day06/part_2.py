with open("puzzle_input") as f:
    puzzle_input = [[cell for cell in line.strip()] for line in f.readlines()]

for y, row in enumerate(puzzle_input):
    if "^" in row:
        x = row.index("^")
        origional_guard_position = (x, y)
        break


def take_step(grid, guard_position):
    x, y = guard_position
    if x < 1 or y < 1:
        raise IndexError
    if grid[y][x] == "^":
        if grid[y - 1][x] == "#":
            grid[y][x] = ">"
        else:
            grid[y - 1][x] = "^"
            guard_position = (x, y - 1)
    elif grid[y][x] == ">":
        if grid[y][x + 1] == "#":
            grid[y][x] = "V"
        else:
            grid[y][x + 1] = ">"
            guard_position = (x + 1, y)
    elif grid[y][x] == "V":
        if grid[y + 1][x] == "#":
            grid[y][x] = "<"
        else:
            grid[y + 1][x] = "V"
            guard_position = (x, y + 1)
    elif grid[y][x] == "<":
        if grid[y][x - 1] == "#":
            grid[y][x] = "^"
        else:
            grid[y][x - 1] = "<"
            guard_position = (x - 1, y)
    return grid, guard_position


import copy
grid = copy.deepcopy(puzzle_input)
visited_cells = set()
guard_position = origional_guard_position
while True:
    try:
        visited_cells.add(guard_position)
        grid, guard_position = take_step(grid, guard_position)
    except IndexError:
        visited_cells.remove(origional_guard_position)
        break


print(len(visited_cells))

iteration_tolerance = 10000
locations_causing_loop = []
visited_cells = list(visited_cells)
for i, (x, y) in enumerate(visited_cells, start=1):
    print(f"Checking [{i}/{len(visited_cells)}] | Blocking ({x},{y}).", end="")
    guard_position = origional_guard_position
    new_grid = copy.deepcopy(puzzle_input)
    new_grid[y][x] = "#"
    iteration = 0
    while True:
        iteration += 1
        try:
            grid, guard_position = take_step(new_grid, guard_position)
        except IndexError:
            print(" -> Cleared")
            break
        if iteration > iteration_tolerance:
            print(" -> Failed")
            locations_causing_loop.append((x, y))
            break
print(len(locations_causing_loop))
