def get_score(them:str, result:str) -> int:
    score = 0

    if result == 'Y':
        score += 3
    elif result == 'Z':
        score += 6

    if them == 'A':
        if result == 'X':
            score += 3
        elif result == 'Y':
            score += 1
        elif result == 'Z':
            score += 2
    elif them == 'B':
        if result == 'X':
            score += 1
        elif result == 'Y':
            score += 2
        elif result == 'Z':
            score += 3
    elif them == 'C':
        if result == 'X':
            score += 2
        elif result == 'Y':
            score += 3
        elif result == 'Z':
            score += 1
    return score

if __name__ == '__main__':
    with open('day_2-input') as f:
        games = f.readlines()

    score = 0
    for game in games:
        game = game.rstrip().split(' ')
        score += get_score(*game)

    print(score)
