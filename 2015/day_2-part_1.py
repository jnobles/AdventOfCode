gift_dimensions = []
with open('day_2-input') as f:
    for line in [x.rstrip() for x in f.readlines()]:
        gift_dimensions.append([int(x) for x in line.split('x')])

paper_needed = 0

for gift in gift_dimensions:
    side_a = gift[0] * gift[1]
    side_b = gift[1] * gift[2]
    side_c = gift[2] * gift[0]
    paper_needed += 2*side_a + 2*side_b + 2*side_c
    paper_needed += min(side_a, side_b, side_c)

print(paper_needed)
