days_to_simulate = 256

with open('day_6-input') as f:
    start_state = [int(x.strip()) for x in f.readline().split(',')]

age_count = [0 for x in range(9)]

for fish in start_state:
    age_count[fish] += 1

for day in range(days_to_simulate):
    births = 0
    for age in range(9):
        if age == 0:
            if age_count[0] > 0:
                births += age_count[0]
        else:
            age_count[age-1] = age_count[age]
    age_count[6] += births
    age_count[8] = births
    print(f'{day+1} {sum(age_count)} {age_count}')
