with open('day_8-input') as f:
    grid = [[int(tree) for tree in line.strip()] for line in f.readlines()]

scenic_score = [[1 for tree in row] for row in grid]

# all edge trees have a scenic score of 0
scenic_score[0] = [0 for tree in scenic_score[0]]
scenic_score[-1] = [0 for tree in scenic_score[-1]]
for row in range(1,len(scenic_score)-1):
    scenic_score[row][0] = 0
    scenic_score[row][-1] = 0

def get_view_count(view:list, tree_height:int):
    if view[-1] >= tree_height:
        return 1
    else:
        score = 1
        while True:
            if len(view) == 1:
                break
            elif view[-1] >= tree_height:
                break
            else:
                score += 1
                view.pop()
    return score

for row in range(1,len(grid)-1):
    for tree in range(1,len(grid[row])-1):
        view = grid[row][:tree]
        scenic_score[row][tree] *= get_view_count(view, grid[row][tree])

        view = grid[row][tree+1:]
        view.reverse()
        scenic_score[row][tree] *= get_view_count(view, grid[row][tree])

grid = [list(x) for x in zip(*grid)]
scenic_score = [list(x) for x in zip(*scenic_score)]

for row in range(1,len(grid)-1):
    for tree in range(1,len(grid[row])-1):
        view = grid[row][:tree]
        scenic_score[row][tree] *= get_view_count(view, grid[row][tree])

        view = grid[row][tree+1:]
        view.reverse()
        scenic_score[row][tree] *= get_view_count(view, grid[row][tree])

grid = [list(x) for x in zip(*grid)]
scenic_score = [list(x) for x in zip(*scenic_score)]

print(max(sum(scenic_score,[])))
