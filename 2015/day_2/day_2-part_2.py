gift_dimensions = []
with open('day_2-input') as f:
    for line in [x.rstrip() for x in f.readlines()]:
        gift_dimensions.append([int(x) for x in line.split('x')])

ribbon_needed = 0

for gift in gift_dimensions:
    gift.sort()
    volume = gift[0] * gift[1] * gift[2]
    perimeter = 2*gift[0] + 2*gift[1]

    ribbon_needed += volume + perimeter

print(ribbon_needed)
