import re

with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]


def is_symbol(pos_x, pos_y):
    try:
        if re.match(r'\d', puzzle_input[pos_y][pos_x]):
            return True
    except IndexError:
        pass
    return False


def check_neighbors(pos_x, pos_y):
    return any([is_symbol(pos_x - 1, pos_y - 1),
                is_symbol(pos_x, pos_y - 1),
                is_symbol(pos_x + 1, pos_y - 1),
                is_symbol(pos_x - 1, pos_y),
                is_symbol(pos_x + 1, pos_y),
                is_symbol(pos_x - 1, pos_y + 1),
                is_symbol(pos_x, pos_y + 1),
                is_symbol(pos_x + 1, pos_y + 1)])


gear_ratio_sum = 0

for i in range(len(puzzle_input)):
    for match in re.finditer(r'\*', puzzle_input[i]):
        if check_neighbors(i, match.start()):
            print(i, match.start())