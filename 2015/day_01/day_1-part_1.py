with open('day_1-input') as f:
    instructions = f.readline().rstrip()

floor = 0
for step in instructions:
    if step == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
