with open('day_7-input') as f:
    crab_positions = [int(x) for x in f.readline().rsplit()[0].split(',')]

locations = [crab_positions.count(i) for i in range(max(crab_positions)+1)]

def calculate_cost(position: int, locations:list) -> int:
    fuel_cost = 0
    for location in range(len(locations)):
        if location == position:
            continue
        else:
            # fuel cost is now the nth triangular number corresponding to
            # the distance traveled. Formula (n(n+1))/2
            distance = abs(location - position)
            fuel_cost += int((distance * (distance + 1)) / 2) * locations[location]
    return fuel_cost

min_fuelcost = calculate_cost(0, locations)
min_fuelcost_pos = 0

for position in range(len(locations)):
    fuel_cost = calculate_cost(position, locations)
    if fuel_cost < min_fuelcost:
        min_fuelcost = fuel_cost
        min_fuelcost_pos = position

print(min_fuelcost, min_fuelcost_pos)
