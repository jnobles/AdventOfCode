priorities = {}
for priority, item in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1):
    priorities[item] = priority


with open('day_3-input') as f:
    rucksacks = [line.rstrip() for line in f.readlines()]

for rucksack in range(len(rucksacks)):
    compartment_size = int(len(rucksacks[rucksack])/2)
    rucksacks[rucksack] = (rucksacks[rucksack][0:compartment_size], rucksacks[rucksack][compartment_size:])

priority_sums = 0
for pouch_1, pouch_2 in rucksacks:
    for item in pouch_1:
        if item in pouch_2:
            priority_sums += priorities[item]
            break

print(priority_sums)
