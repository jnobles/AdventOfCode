with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

import re

powerset_sum = 0

for line in puzzle_input:
    min_red = 0
    min_green = 0
    min_blue = 0
    rounds = line.split(':')[1].split(';')
    for pull in rounds:
        reds = re.search(r'(\d+) red', pull)
        reds = int(reds.group(1)) if reds else 0
        greens = re.search(r'(\d+) green', pull)
        greens = int(greens.group(1)) if greens else 0
        blues = re.search(r'(\d+) blue', pull)
        blues = int(blues.group(1)) if blues else 0

        min_red = max(min_red, reds)
        min_green = max(min_green, greens)
        min_blue = max(min_blue, blues)
    powerset_sum += (min_red * min_green * min_blue)
print(powerset_sum)