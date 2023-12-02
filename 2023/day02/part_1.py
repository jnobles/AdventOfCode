with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

import re

bag = {'red': 12, 'green': 13, 'blue': 14}

possible_games_sum = 0

for line in puzzle_input:
    valid_game = True
    game_id = int(re.search(r'Game (\d+):', line).group(1))
    rounds = line.split(':')[1].split(';')
    for pull in rounds:
        reds = re.search(r'(\d+) red', pull)
        reds = int(reds.group(1)) if reds else 0
        greens = re.search(r'(\d+) green', pull)
        greens = int(greens.group(1)) if greens else 0
        blues = re.search(r'(\d+) blue', pull)
        blues = int(blues.group(1)) if blues else 0

        if reds > bag['red'] or greens > bag['green'] or blues > bag['blue']:
            valid_game = False
            break
    possible_games_sum += game_id if valid_game else 0
print(possible_games_sum)