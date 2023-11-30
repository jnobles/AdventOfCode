priorities = {}
for priority, item in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1):
    priorities[item] = priority


with open('day_3-input') as f:
    rucksacks = [line.rstrip() for line in f.readlines()]

priority_sum = 0

for i in range(0,len(rucksacks),3):
    for item in rucksacks[i]:
        if item in rucksacks[i+1] and item in rucksacks[i+2]:
            priority_sum += priorities[item]
            break

print(priority_sum)
