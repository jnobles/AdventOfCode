with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

import re

calibration_sum = 0
for line in puzzle_input:
    calibration_value = re.search(r'(\d)', line).group(1)
    calibration_value += re.search(r'(\d)', line[::-1]).group(1)
    calibration_sum += int(calibration_value)

print(calibration_sum)
