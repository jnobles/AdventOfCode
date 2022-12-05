with open('day_4-input') as f:
    assignment_pairs = [item.rstrip() for item in f.readlines()]

redundant_count = 0

for pair in assignment_pairs:
    elf_1, elf_2 = [[int(x) for x in item.split('-')] for item in pair.split(',')]
    for i in range(elf_1[0], elf_1[1]+1):
        if i in range(elf_2[0], elf_2[1]+1):
            redundant_count += 1
            break

print(redundant_count)
