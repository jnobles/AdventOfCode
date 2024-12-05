with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

xmas_count = 0
for y in range(1, len(puzzle_input)-1):
    for x in range(1, len(puzzle_input[0])-1):
        if puzzle_input[y][x] == "A":
            mas_count = [
                puzzle_input[y-1][x-1] + puzzle_input[y][x] + puzzle_input[y+1][x+1] == "MAS",
                puzzle_input[y-1][x+1] + puzzle_input[y][x] + puzzle_input[y+1][x-1] == "MAS",
                puzzle_input[y+1][x+1] + puzzle_input[y][x] + puzzle_input[y-1][x-1] == "MAS",
                puzzle_input[y+1][x-1] + puzzle_input[y][x] + puzzle_input[y-1][x+1] == "MAS"]
            xmas_count += sum(mas_count) >= 2
print(xmas_count)
