with open("puzzle_input") as f:
    puzzle_input = [line.split() for line in f.readlines()]

farm = [[plot for plot in line[0]] for line in puzzle_input]

from collections import Counter
perimeters = Counter()
areas = Counter()

plant_index = 0


def flood(x, y, plant, plant_index):
    if x < 0 or x >= len(farm[0]) or y < 0 or y >= len(farm):
        return
    if farm[y][x] != plant:
        return
    farm[y][x] = plant_index
    flood(x+1, y, plant, plant_index)
    flood(x-1, y, plant, plant_index)
    flood(x, y+1, plant, plant_index)
    flood(x, y-1, plant, plant_index)


for y in range(len(farm)):
    for x in range(len(farm[0])):
        if type(farm[y][x]) is str:
            flood(x, y, farm[y][x], plant_index)
            plant_index += 1


for y, row in enumerate(farm):
    for x, plot in enumerate(row):
        areas[plot] += 1
        directions = [[x, y+1], [x, y-1], [x-1, y], [x+1, y]]
        for x, y in directions:
            try:
                if x < 0 or y < 0:
                    raise IndexError
                if farm[y][x] != plot:
                    perimeters[plot] += 1
            except IndexError:
                perimeters[plot] += 1

cost = 0
for plant in areas.keys():
    cost += areas[plant] * perimeters[plant]

print(cost)
