import re

with open('day_15-input') as f:
    data = [line.rstrip() for line in f.readlines()]

def get_distance(x:int, y:int, a:int, b:int) -> int:
    return abs(x-a) + abs(y-b)

target_line = 2000000

#min_x, max_x = 0, 0
#for line in data:
#    coords = re.findall(r'x=(-*\d*)', line)
#    sensor_x, beacon_x = [int(_) for _ in coords]
#    min_x = min(min_x, sensor_x, beacon_x)
#    max_x = max(max_x, sensor_x, beacon_x)

#potential_indicies = [i for i in range(min_x, max_x+1)]
blocked_indicies = []
for line in data:
    coords = re.finditer(r'x=(-*\d*), y=(-*\d*)', line)
    sensor_x, sensor_y = [int(_) for _ in next(coords).groups()]
    beacon_x, beacon_y = [int(_) for _ in next(coords).groups()]
    distance = get_distance(sensor_x, sensor_y, beacon_x, beacon_y)
    print(target_line in range(sensor_y-distance, sensor_y+distance+1))
    if target_line in range(sensor_y-distance, sensor_y+distance+1):
        width = distance - abs(sensor_y - target_line)
        for i in range(sensor_x-width, sensor_x+width):
            print(f'{sensor_x-width}, {sensor_x+width} -- {i}')
            if i not in blocked_indicies:
                blocked_indicies.append(i)

print(len(blocked_indicies))

# look into only tracking the edges of the blocked region, rather than the whole region itself



#import re
#
#class Sensor:
#    def __init__(self, sensor_x:str, sensor_y:str, beacon_x:str, beacon_y:str):
#        self.x = int(sensor_x)
#        self.y = int(sensor_y)
#        self.beacon_x = int(beacon_x)
#        self.beacon_y = int(beacon_y)
#
#    def get_coverage(self) -> list[list[int]]:
#        distance = Sensor.get_distance(self.x, self.y, self.beacon_x, self.beacon_y)
#        min_x = self.x - distance
#        min_y = self.y - distance
#        max_x = self.x + distance
#        max_y = self.y + distance
#
#        coverage = []
#        for y in range(min_y, max_y+1):
#            for x in range(min_x, max_x+1):
#                if Sensor.get_distance(self.x, self.y, x, y) <= distance:
#                    if x < 0 or y < 0:
#                        continue
#                    coverage.append([x, y])
#
#        return coverage
#
#    @staticmethod
#    def get_distance(x:int, y:int, a:int, b:int) -> int:
#        return abs(x-a) + abs(y-b)
#
#with open('day_15-input') as f:
#    data = [line.rstrip() for line in f.readlines()]
#
#sensors = []
#for line in data:
#    coords = re.finditer(r'x=(-*\d*), y=(-*\d*)', line)
#    sensor_x, sensor_y = next(coords).groups()
#    beacon_x, beacon_y = next(coords).groups()
#    sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))
#
#min_x,  min_y, max_x, max_y = 0, 0, 0, 0
#for sensor in sensors:
#    min_x = min(min_x, sensor.x, sensor.beacon_x)
#    min_y = min(min_y, sensor.y, sensor.beacon_y)
#    max_x = max(max_x, sensor.x, sensor.beacon_x)
#    max_y = max(max_y, sensor.y, sensor.beacon_y)
#
#for sensor in sensors:
#    sensor.x -= min_x
#    sensor.y -= min_y
#    sensor.beacon_x -= min_x
#    sensor.beacon_y -= min_y
#
#grid = []
#for y in range(max_y+1 - min_y):
#    grid.append([])
#    for x in range(max_x+1 - min_x):
#        grid[y].append('░')
#
#for sensor in sensors:
#    for x, y in sensor.get_coverage():
#        try:
#            if grid[y][x] == 'S' or grid[y][x] == 'B':
#                continue
#            grid[y][x] = '█'
#        except IndexError:
#            continue
#    grid[sensor.y][sensor.x] = 'S'
#    grid[sensor.beacon_y][sensor.beacon_x] = 'B'
#
#sum = 0
#for i in grid[10]:
#    if i == '█':
#        sum += 1
#print(sum)
#
