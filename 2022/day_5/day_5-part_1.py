with open('day_5-input') as f:
    puzzle_input = [item.rstrip('\n') for item in f.readlines()]

stack_count = int(puzzle_input[puzzle_input.index('')-1].split()[-1])
steps = puzzle_input[puzzle_input.index('')+1:]
stacks = [[] for i in range(stack_count)]

for line in puzzle_input[puzzle_input.index('')-2::-1]:
    for i in range(0,len(line),4):
        if line[i:i+4].strip() != '':
            stacks[i//4].append(line[i:i+4])

for step in steps:
    _, quant, _, start, _, end = step.split()
    quant = int(quant)
    start = int(start) - 1
    end = int(end) - 1
    temp = []
    for i in range(quant):
        temp.append(stacks[start].pop())
    temp.reverse()
    while temp:
        stacks[end].append(temp.pop())

top_row = ' '.join([stack[-1].strip() for stack in stacks])
top_row = [item.strip('[').strip(']') for item in top_row.split()]
top_row = ''.join(top_row)

print(top_row)