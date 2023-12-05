with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in puzzle_input.pop(0).split(':')[1].split()]

print('seeds:')
print(seeds)
puzzle_input.pop(0)
print(puzzle_input.pop(0))

while puzzle_input:
    values = [int(_) for _ in puzzle_input.pop(0).split()]
    destination = list(range(values[0], values[0] + values[2]))
    source = list(range(values[1], values[1] + values[2]))
    for i, seed in enumerate(seeds):
        if seed in source:
            seeds[i] = destination[source.index(seed)]
    try:
        if puzzle_input[0] == '':
            print(seeds)
            puzzle_input.pop(0)
            print(puzzle_input.pop(0))
    except IndexError:
        pass
print(seeds)
