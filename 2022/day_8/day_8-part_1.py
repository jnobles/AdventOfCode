with open('day_8-input') as f:
    grid = [[int(tree) for tree in line.strip()] for line in f.readlines()]

is_visible = [[False for tree in row] for row in grid]

# all edge trees are visible
is_visible[0] = [True for tree in is_visible[0]]
is_visible[-1] = [True for tree in is_visible[-1]]
for row in range(len(is_visible)):
    is_visible[row][0] = True
    is_visible[row][-1] = True

for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        if grid[y][x] > max(grid[y][0:x]) or grid[y][x] > max(grid[y][x+1:]):
            is_visible[y][x] = True

grid = [list(x) for x in zip(*grid)]
is_visible = [list(x) for x in zip(*is_visible)]

for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        if grid[y][x] > max(grid[y][0:x]) or grid[y][x] > max(grid[y][x+1:]):
            is_visible[y][x] = True

grid = [list(x) for x in zip(*grid)]
is_visible = [list(x) for x in zip(*is_visible)]

is_visible = sum(is_visible, [])
print(sum(is_visible))