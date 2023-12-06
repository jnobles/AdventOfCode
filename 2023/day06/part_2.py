with open('practice_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

time = int(''.join(puzzle_input[0].split()[1:]))
distance = int(''.join(puzzle_input[1].split()[1:]))

min_range = []
max_range = []
min_found = False

step = 1000
for time_pressed in range(0, time, step):
    print((time_pressed * (time - time_pressed)) > distance and not min_found, end=' ')
    print(min_found and not (time_pressed * (time - time_pressed)) > distance)
    if (time_pressed * (time - time_pressed)) > distance and not min_found:
        min_range = [time_pressed - step, time_pressed]
        min_found = True
    elif min_found and not (time_pressed * (time - time_pressed)) > distance:
        max_range = [time_pressed - step, time_pressed]

for i in range(min_range[0], min_range[1]):
    if i * (time - i) > distance:
        min_range = i
        break

print(min_range)
print(max_range)