with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in puzzle_input.pop(0).split(':')[1].split()]
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

for line in puzzle_input[2:]:
    try:
        int(line[0])
    except (IndexError, ValueError):
        pass
    else:
        destination, source, span = [int(_) for _ in line.split()]
        for i, seed in enumerate(seeds):
            #print(seed, list(range(source, source + span)))
            if seed in range(source, source + span):
                print(seeds)
                source = list(range(source, source + span))
                destination = list(range(destination, destination + span))
                seeds[i] = destination[source.index(seeds[i])]
                #print(seeds)

print(seeds)

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
