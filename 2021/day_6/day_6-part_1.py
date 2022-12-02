days_to_simulate = 80

days = [[] for day in range(days_to_simulate + 1)]

with open('day_6-input') as f:
    days[0] = [int(x.strip()) for x in f.readline().split(',')]

day = 0
while day < days_to_simulate:
    for fish in days[day]:
        days[day+1].append(fish)

    for i in range(len(days[day+1])):
        days[day+1][i] -= 1

    for i in range(len(days[day+1])):
        if days[day+1][i] < 0:
            days[day+1][i] = 6
            days[day+1].append(8)

    day += 1

print(len(days[-1]))
