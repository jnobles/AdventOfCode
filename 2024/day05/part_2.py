with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

rules = []
printings = []

split_index = puzzle_input.index("")
for line in puzzle_input[:split_index]:
    rules.append([int(_) for _ in line.split("|")])
for line in puzzle_input[split_index+1:]:
    printings.append([int(_) for _ in line.split(",")])

incorrect_printings = []
while printings:
    printing = printings.pop()
    for rule in rules:
        if rule[0] in printing and rule[1] in printing:
            if printing.index(rule[0]) > printing.index(rule[1]):
                incorrect_printings.append(printing)
                break

for printing in incorrect_printings:
    while True:
        correct_printing = True
        for rule in rules:
            if rule[0] in printing and rule[1] in printing:
                if printing.index(rule[0]) > printing.index(rule[1]):
                    correct_printing = False
                    a = printing.index(rule[0])
                    b = printing.index(rule[1])
                    tmp = printing[a]
                    printing[a] = printing[b]
                    printing[b] = tmp
        if correct_printing:
            break

middle_sum = 0
for printing in incorrect_printings:
    middle_index = (len(printing) // 2)
    middle_sum += printing[middle_index]

print(middle_sum)
