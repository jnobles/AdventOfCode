elves = []

with open('day_1-input') as f:
    inventory = []
    while True:
        line = f.readline()
        if line == '':
            break
        if line == '\n':
            elves.append([item for item in inventory])
            inventory = []
        else:
            inventory.append(int(line.rstrip()))
    elves.append([item for item in inventory])

print(max([sum(list) for list in elves]))