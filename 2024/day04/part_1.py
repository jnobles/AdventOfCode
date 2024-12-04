with open("practice_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

xmas_count = 0
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[0])):
        if puzzle_input[y][x] == "X":
            try:
                search_right = all([
                    puzzle_input[y][x+1] == "M",
                    puzzle_input[y][x+2] == "A",
                    puzzle_input[y][x+3] == "S"])
            except IndexError:
                search_right = False
            try:
                search_down_right = all([
                    puzzle_input[y+1][x+1] == "M",
                    puzzle_input[y+2][x+2] == "A",
                    puzzle_input[y+3][x+3] == "S"])
            except IndexError:
                search_down_right = False
            try:
                search_down = all([
                    puzzle_input[y+1][x] == "M",
                    puzzle_input[y+2][x] == "A",
                    puzzle_input[y+3][x] == "S"])
            except IndexError:
                search_down = False
            try:
                search_down_left = all([
                    puzzle_input[y+1][x-1] == "M",
                    puzzle_input[y+2][x-2] == "A",
                    puzzle_input[y+3][x-3] == "S"])
            except IndexError:
                search_down_left = False
            try:
                search_left = all([
                    puzzle_input[y][x-1] == "M",
                    puzzle_input[y][x-2] == "A",
                    puzzle_input[y][x-3] == "S"])
            except IndexError:
                search_left = False
            try:
                search_up_left = all([
                    puzzle_input[y-1][x-1] == "M",
                    puzzle_input[y-2][x-2] == "A",
                    puzzle_input[y-3][x-3] == "S"])
            except IndexError:
                search_up_left = False
            try:
                search_up = all([
                    puzzle_input[y-1][x] == "M",
                    puzzle_input[y-2][x] == "A",
                    puzzle_input[y-3][x] == "S"])
            except IndexError:
                search_up = False
            try:
                search_up_right = all([
                    puzzle_input[y-1][x+1] == "M",
                    puzzle_input[y-2][x+2] == "A",
                    puzzle_input[y-3][x+3] == "S"])
            except IndexError:
                search_up_right = False
            print(x, y)
            print([search_right, search_down_right, search_down, search_down_left, search_left, search_up_left, search_up, search_up_right])

            xmas_count += sum([search_right, search_down_right, search_down, search_down_left, search_left, search_up_left, search_up, search_up_right])
print(xmas_count)
