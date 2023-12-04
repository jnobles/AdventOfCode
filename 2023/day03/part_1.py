import re

with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]


def is_symbol(pos_x, pos_y):
    try:
        if re.match(r'[^.\d]', puzzle_input[pos_y][pos_x]):
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


part_number_sum = 0

for i in range(len(puzzle_input)):
    for match in re.finditer(r'(\d+)', puzzle_input[i]):
        is_finished = False
        for j in range(match.start(), match.end()):
            if check_neighbors(j, i) and not is_finished:
                part_number_sum += int(match.group(1))
                is_finished = True
print(part_number_sum)
