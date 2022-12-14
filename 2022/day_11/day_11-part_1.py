class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.times_inspected = 0
        self.throw_test = None
        self.throw_on_true = None
        self.throw_on_false = None

    def inspect(self, item):
        self.times_inspected += 1
        print(f'inspects {item}')
        return self.operation(item) // 3

    def take_turn(self):
        while len(self.items) > 0:
            current_item = self.inspect(self.items.pop(0))
            try:
                int(current_item) / self.throw_test
            except ValueError:
                self.throw_on_false.items.append(current_item)
            else:
                self.throw_on_true.items.append(current_item)

    @staticmethod
    def pull_value(string:str) -> int:
        value = None
        for i in range(len(string)-1, 0, -1):
            try:
                value = int(string[i:])
            except ValueError:
                break
        return value

with open('day_11-input-practice') as f:
    lines = [line.strip() for line in f.readlines()]

monkeys = [Monkey() for i in range((len(lines)+1)//7)]
for i in range(0, len(lines), 7):
    monkeys[i//7].items = [int(item) for item in lines[i+1].split(':')[1].split(',')]
    monkeys[i//7].operation = lambda old: eval(lines[i+2].split(':')[1].split('=')[1])
    monkeys[i//7].throw_test = Monkey.pull_value(lines[i+3])
    monkeys[i//7].throw_on_true = monkeys[Monkey.pull_value(lines[i+4]) - 1]
    monkeys[i//7].throw_on_false = monkeys[Monkey.pull_value(lines[i+5]) - 1]

number_of_rounds = 20
for round in range(number_of_rounds):
    for monkey in monkeys:
        monkey.take_turn()