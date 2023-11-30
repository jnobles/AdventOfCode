increase_count = 0

with open('input_1') as f:
    moving_range = [int(f.readline()),int(f.readline()),int(f.readline())]
    previous_sum = sum(moving_range)

    for line in f.readlines():
        moving_range.pop(0)
        moving_range.append(int(line))
        if sum(moving_range) > previous_sum:
            increase_count += 1
        previous_sum = sum(moving_range)

print(increase_count)
