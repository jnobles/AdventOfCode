with open('day_8-input') as f:
    sequences = [tuple([x.strip() for x in line.split('|')]) for line in f.readlines()]

sum_1_4_7_8 = 0

for seq_in, seq_out in sequences:
    for display in seq_out.split(' '):
        if len(display) == 2 or len(display) == 3 or len(display) == 4 or len(display) == 7:
            sum_1_4_7_8 += 1

print(sum_1_4_7_8)
