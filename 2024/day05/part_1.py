with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

rules = []
printings = []

split_index = puzzle_input.index("")
for line in puzzle_input[:split_index]:
    rules.append([int(_) for _ in line.split("|")])
for line in puzzle_input[split_index+1:]:
    printings.append([int(_) for _ in line.split(",")])

correct_printings = []
while printings:
    correct_printing = True
    printing = printings.pop()
    for rule in rules:
        if rule[0] in printing and rule[1] in printing:
            if printing.index(rule[0]) > printing.index(rule[1]):
                correct_printing = False
                break
    if correct_printing:
        correct_printings.append(printing)

middle_sum = 0
for printing in correct_printings:
    middle_index = (len(printing) // 2)
    middle_sum += printing[middle_index]

print(middle_sum)
