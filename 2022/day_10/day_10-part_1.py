with open('day_10-input') as f:
    commands = [line.rstrip() for line in f.readlines()]

class CPU:
    def __init__(self, first_report, report_frequency):
        self.clock_cycle = 0
        self.qeued_commands = []
        self.cycles_to_next_report = first_report
        self.report_frequency = report_frequency
        self.current_signal_strength = None
        self.stored_signal_strengths = []
        self.current_command = None
        self.register = 1

    def load_commands(self, commands:list):
        commands.reverse()
        self.qeued_commands = commands

    def tick(self):
        self.clock_cycle += 1
        self.current_signal_strength = self.clock_cycle * self.register
        if self.cycles_to_next_report == 1:
            self.stored_signal_strengths.append(self.current_signal_strength)
            self.cycles_to_next_report = self.report_frequency
        else:
            self.cycles_to_next_report -= 1

    def addx(self, value):
        self.tick()
        self.tick()
        self.register += int(value)

    def noop(self):
        self.tick()

    def run(self):
        while len(commands) > 0:
            self.current_command = self.qeued_commands.pop()
            if self.current_command == 'noop':
                self.noop()
            else:
                self.addx(self.current_command.split()[1])


cpu = CPU(first_report=20, report_frequency=40)
cpu.load_commands(commands)
cpu.run()

print(sum(cpu.stored_signal_strengths))
