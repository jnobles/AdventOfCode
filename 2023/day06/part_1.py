with open('puzzle_input') as f:
    puzzle_input = [line.strip() for line in f.readlines()]

times = [int(time) for time in puzzle_input[0].split()[1:]]
distances = [int(distance) for distance in puzzle_input[1].split()[1:]]

total_ways_to_win = 1
for race in range(len(times)):
    ways_to_win = 0
    results = []
    for i in range(times[race]):
        speed = i
        results.append(speed * (times[race] - speed))
    results.append(0)  # for holding the button the entire time

    for result in results:
        if result > distances[race]:
            ways_to_win += 1
    total_ways_to_win *= ways_to_win
print(total_ways_to_win)
