import math

with open('day_9-input') as f:
    steps = [line.rstrip() for line in f.readlines()]

for item, step in enumerate(steps):
    direction, distance = step.split()[0], int(step.split()[1])
    if direction == 'R':
        instruction = ('x', distance)
    elif direction == 'L':
        instruction = ('-x', distance)
    elif direction == 'U':
        instruction = ('y', distance)
    elif direction == 'D':
        instruction = ('-y', distance)
    steps[item] = instruction

class Knot():
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.name = name
        self.visited = ['(0,0)']
        self.next_knot = None

    def __repr__(self):
        return f'{self.name}: ({self.x},{self.y})'

    def __str__(self):
        return f'{self.name}: ({self.x},{self.y})'

    @staticmethod
    def get_distance(a, b, x, y):
        return math.sqrt(math.pow(a - x, 2) + math.pow(b - y, 2))

    def add_chain(self, next_knot):
        self.next_knot = next_knot

    def move(self, direction, distance):
        while distance > 0:
            if direction == 'x':
                self.x += 1
            elif direction == '-x':
                self.x -= 1
            elif direction == 'y':
                self.y += 1
            elif direction == '-y':
                self.y -= 1

            if f'({self.x},{self.y})' not in self.visited:
                self.visited.append(f'({self.x},{self.y})')

            if self.next_knot != None:
                self.next_knot.follow(self)

            distance -= 1

    def follow(self, leading_knot):
        distance = Knot.get_distance(self.x, self.y, leading_knot.x, leading_knot.y)
        should_move = True if distance > 1.5 else False

        if should_move:
            if leading_knot.x == self.x:
                if leading_knot.y > self.y:
                    self.y += 1
                elif leading_knot.y < self.y:
                    self.y -= 1
            elif leading_knot.y == self.y:
                if leading_knot.x > self.x:
                    self.x += 1
                elif leading_knot.x < self.x:
                    self.x -= 1
            else:
                if leading_knot.x > self.x and leading_knot.y > self.y:
                    self.x += 1
                    self.y += 1
                elif leading_knot.x < self.x and leading_knot.y > self.y:
                    self.x -= 1
                    self.y += 1
                elif leading_knot.x > self.x and leading_knot.y < self.y:
                    self.x += 1
                    self.y -= 1
                elif leading_knot.x < self.x and leading_knot.y < self.y:
                    self.x -= 1
                    self.y -= 1

            if f'({self.x},{self.y})' not in self.visited:
                    self.visited.append(f'({self.x},{self.y})')

            if self.next_knot != None:
                self.next_knot.follow(self)


knots = [Knot(name=i) for i in range(10)]
for knot in range(len(knots)):
    try:
        knots[knot].add_chain(knots[knot+1])
    except IndexError:
        break

for direction, distance in steps:
    knots[0].move(direction, distance)

print(len(knots[-1].visited))
