import re

with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]


gear_ratio_sum = 0

for i in range(len(puzzle_input)):
    for match in re.finditer(r'\*', puzzle_input[i]):
        touching_parts = []
        for part in re.finditer(r'(\d+)', puzzle_input[i - 1]):
            left, right = part.span()
            if match.start() in range(left-1, right+1):
                touching_parts.append(int(part.group(1)))
        for part in re.finditer(r'(\d+)', puzzle_input[i]):
            left, right = part.span()
            if match.start() in range(left-1, right+1):
                touching_parts.append(int(part.group(1)))
        for part in re.finditer(r'(\d+)', puzzle_input[i + 1]):
            left, right = part.span()
            if match.start() in range(left-1, right+1):
                touching_parts.append(int(part.group(1)))
        if len(touching_parts) == 2:
            gear_ratio_sum += touching_parts[0] * touching_parts[1]
print(gear_ratio_sum)
