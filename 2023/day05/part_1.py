with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in puzzle_input[0].split(':')[1].split()]
puzzle_input = puzzle_input[3:]

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

mapping = []
for step in steps:
    for line in step:
        dst, src, span = [int(_) for _ in line.split()]
        dst_list = range(dst, dst + span)
        src = range(src, src + span)

pass
#seeds = [int(seed) for seed in puzzle_input.pop(0).split(':')[1].split()]
#map_dict = {}
#for line in puzzle_input[2:]:
#    try:
#        int(line[0])
#    except (IndexError, ValueError):
#        for i, seed in enumerate(seeds):
#            if seed in map_dict:
#                seeds[i] = map_dict[seed]
#        map_dict = {}
#        print(seeds)
#    else:
#        destination, source, span = [int(_) for _ in line.split()]
#        for i in range(span):
#            map_dict[source+i] = destination+i

#mappings = [[]]
#group = 0
#for line in puzzle_input[2:]:
#    try:
#        int(line[0])
#    except (IndexError, ValueError):
#        group += 1
#    else:
#        mappings[group].append([int(_) for _ in line.split()])


#for line in puzzle_input[2:]:
#    try:
#        int(line[0])
#    except (IndexError, ValueError):
#        pass
#    else:
#        destination, source, span = [int(_) for _ in line.split()]
#        for i, seed in enumerate(seeds):
#            if seed in range(source, source + span):
#                print(seeds)
#                source_list = list(range(source, source + span))
#                destination_list = list(range(destination, destination + span))
#                print(source_list, destination_list, sep='\n')
#                seeds[i] = destination_list[source_list.index(seeds[i])]
#
#print(seeds)

#while puzzle_input:
#    values = [int(_) for _ in puzzle_input.pop(0).split()]
#    destination = list(range(values[0], values[0] + values[2]))
#    source = list(range(values[1], values[1] + values[2]))
#    for i, seed in enumerate(seeds):
#        if seed in source:
#            seeds[i] = destination[source.index(seed)]
#    try:
#        if puzzle_input[0] == '':
#            print(seeds)
#            puzzle_input.pop(0)
#            print(puzzle_input.pop(0))
#    except IndexError:
#        pass
#print(seeds)
