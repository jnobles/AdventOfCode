with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

import re

def to_digit(x):
    if re.match(r'\d', x):
        return x
    else:
        match x:
            case 'one': return '1'
            case 'two': return '2'
            case 'three': return '3'
            case 'four': return '4'
            case 'five': return '5'
            case 'six': return '6'
            case 'seven': return '7'
            case 'eight': return '8'
            case 'nine': return '9'


calibration_sum = 0
for line in puzzle_input:
    calibration_value_1 = re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(1)
    calibration_value_2 = re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)'
                                    r'(?!.*(?:\d|one|ne|two|wo|three|hree|four|our|five|ive|six|ix|seven|even|eight|ight|nine|ine))', line).group(1)
    value = (int(to_digit(calibration_value_1) + to_digit(calibration_value_2)))
    calibration_sum += int(to_digit(calibration_value_1) + to_digit(calibration_value_2))

print(calibration_sum)
