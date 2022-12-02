diag_report = []

with open('day_3-input') as f:
    for line in f:
        diag_report.append(line.rstrip())

o2_rating = diag_report
co2_rating = diag_report

for place in range(len(o2_rating[0])):
    if len(o2_rating) == 1:
        break
    count_1 = 0
    count_0 = 0
    for line in o2_rating:
        if line[place:place+1] == '1':
            count_1 += 1
        else:
            count_0 += 1
    most_common = '1' if count_1 >= count_0 else '0'
    o2_rating = [line for line in o2_rating if line[place:place+1] == most_common]

for place in range(len(co2_rating[0])):
    if len(co2_rating) == 1:
        break

    count_1 = 0
    count_0 = 0
    for line in co2_rating:
        if line[place:place+1] == '1':
            count_1 += 1
        else:
            count_0 += 1
    least_common = '1' if count_1 < count_0 else '0'
    co2_rating = [line for line in co2_rating if line[place:place+1] == least_common]

o2_rating = int(o2_rating[0],2)
co2_rating = int(co2_rating[0],2)

print(o2_rating*co2_rating)
