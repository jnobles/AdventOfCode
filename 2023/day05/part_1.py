with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in puzzle_input[0].split(':')[1].split()]
puzzle_input = puzzle_input[3:]
puzzle_input.append(':(')

steps = []
temp = []
for line in puzzle_input:
    try:
        int(line[0])
    except IndexError:
        pass
    except ValueError:
        steps.append(temp)
        temp = []
    else:
        temp.append(line)

mappings = {}
print(seeds)
for step in steps:
    mappings = {}
    for line in step:
        dst, src, span = [int(_) for _ in line.split()]
        dst_list = list(range(dst, dst + span))
        src_list = list(range(src, src + span))
        for i, item in enumerate(src_list):
            mappings[item] = dst_list[i]
    for i, seed in enumerate(seeds):
        if seed in mappings:
            seeds[i] = mappings[seed]
    print(seeds)
print(min(seeds))

