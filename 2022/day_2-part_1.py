def get_score(them:str, you:str) -> int:
    score = 0

    if you == 'X':
        score += 1
    elif you == 'Y':
        score += 2
    elif you == 'Z':
        score += 3

    if (them == 'A' and you == 'X') or (them == 'B' and you == 'Y') or (them == 'C' and you == 'Z'):
        score += 3
    elif (them == 'A' and you == 'Y') or (them == 'B' and you == 'Z') or (them == 'C' and you == 'X'):
        score += 6
    return score

if __name__ == '__main__':
    with open('day_2-input') as f:
        games = f.readlines()

    score = 0
    for game in games:
        game = game.rstrip().split(' ')
        score += get_score(*game)

    print(score)
