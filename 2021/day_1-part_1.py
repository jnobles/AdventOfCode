increase_count = 0
previous_value = 0
with open('input_1') as f:
    previous_value = int(f.readline())
    for line in f.readlines():
        if int(line) > previous_value:
            increase_count += 1
        previous_value = int(line)
print(increase_count)
