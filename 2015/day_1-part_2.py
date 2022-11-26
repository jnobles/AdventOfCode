with open('day_1-input') as f:
    instructions = f.readline().rstrip()

floor = 0
for step in range(len(instructions)):
    if instructions[step] == '(':
        floor += 1
    else:
        floor -= 1
        if floor < 0:
            break

print(step+1)
