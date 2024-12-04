with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

left = []
right = []

for item in puzzle_input:
    item_1, item_2 = item.split("   ")
    left.append(int(item_1))
    right.append(int(item_2))

left.sort()
right.sort()

total_distance = 0
for i in range(len(left)):
    total_distance += abs(left[i] - right[i])

print(total_distance)
