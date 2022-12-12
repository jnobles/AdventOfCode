with open('day_10-input') as f:
    commands = [line.rstrip() for line in f.readlines()]

class CPU:
    def __init__(self, first_report, report_frequency):
        self.clock_cycle = 0
        self.qeued_commands = []
        self.cycles_to_next_report = first_report
        self.report_frequency = report_frequency
        self.current_command = None
        self.register = 1
        self.monitor = CRT(resolution=40)

    def load_commands(self, commands:list):
        commands.reverse()
        self.qeued_commands = commands

    def tick(self):
        self.clock_cycle += 1
        self.monitor.display(self.register)

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


class CRT:
    def __init__(self, resolution):
        self.resolution = resolution
        self.current_pixel = 0

    def display(self, active_register):
        active_pixels = [active_register-1, active_register, active_register+1]
        if self.current_pixel in active_pixels:
            print('#',end='')
        else:
            print('.',end='')

        if self.current_pixel == self.resolution - 1:
            print()
            self.current_pixel = 0
        else:
            self.current_pixel += 1


cpu = CPU(first_report=20, report_frequency=40)

cpu.load_commands(commands)
cpu.run()

print(sum(cpu.stored_signal_strengths))
