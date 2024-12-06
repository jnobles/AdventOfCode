with open("puzzle_input") as f:
    puzzle_input = [[cell for cell in line.strip()] for line in f.readlines()]

for y, row in enumerate(puzzle_input):
    if "^" in row:
        x = row.index("^")
        guard_position = (x, y)
        break

while True:
    x, y = guard_position
    try:
        if x < 1 or y < 1:
            raise IndexError
        if puzzle_input[y][x] == "^":
            if puzzle_input[y-1][x] == "#":
                puzzle_input[y][x] = ">"
            else:
                puzzle_input[y-1][x] = "^"
                puzzle_input[y][x] = "X"
                guard_position = (x, y-1)
        elif puzzle_input[y][x] == ">":
            if puzzle_input[y][x+1] == "#":
                puzzle_input[y][x] = "V"
            else:
                puzzle_input[y][x+1] = ">"
                puzzle_input[y][x] = "X"
                guard_position = (x+1, y)
        elif puzzle_input[y][x] == "V":
            if puzzle_input[y+1][x] == "#":
                puzzle_input[y][x] = "<"
            else:
                puzzle_input[y+1][x] = "V"
                puzzle_input[y][x] = "X"
                guard_position = (x, y+1)
        elif puzzle_input[y][x] == "<":
            if puzzle_input[y][x-1] == "#":
                puzzle_input[y][x] = "^"
            else:
                puzzle_input[y][x-1] = "<"
                puzzle_input[y][x] = "X"
                guard_position = (x-1, y)
    except IndexError:
        puzzle_input[y][x] = "X"
        break

print(sum(row.count("X") for row in puzzle_input))
