gamma_bits = ''
epsilon_bits = ''
diag_report = [[] for i in range(12)]

with open('day_3-input') as f:
    for line in f:
        for i in range(12):
            diag_report[i].append(line[i])

for group in diag_report:
    if group.count('1') > group.count('0'):
        gamma_bits = ''.join([gamma_bits, '1'])
        epsilon_bits = ''.join([epsilon_bits, '0'])
    else:
        gamma_bits = ''.join([gamma_bits, '0'])
        epsilon_bits = ''.join([epsilon_bits, '1'])

gamma_rate = int(gamma_bits, 2)
epsilon_rate = int(epsilon_bits, 2)

print(gamma_rate * epsilon_rate)

gamma_bits = ''
epsilon_bits = ''
diag_report = []

with open('day_3-input') as f:
    for line in f:
        diag_report.append(line)

for i in range(len(diag_report[0])):
    count_1 = 0
    count_0 = 0
    for j in range(len(diag_report)):
        print(diag_report[j][i:i+1])
        if diag_report[j][i:i+1] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_1 > count_0:
        gamma_bits = ''.join([gamma_bits, '1'])
        epsilon_bits = ''.join([epsilon_bits, '0'])
    else:
        gamma_bits = ''.join([gamma_bits, '0'])
        epsilon_bits = ''.join([epsilon_bits, '1'])

gamma_rate = int(gamma_bits, 2)
epsilon_rate = int(epsilon_bits, 2)

print(gamma_rate * epsilon_rate)
