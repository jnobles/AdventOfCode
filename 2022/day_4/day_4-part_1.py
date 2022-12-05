with open('day_4-input') as f:
    assignment_pairs = [item.rstrip() for item in f.readlines()]

redundant_count = 0

for pair in assignment_pairs:
    elf_1, elf_2 = [[int(x) for x in item.split('-')] for item in pair.split(',')]
    if elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]:
        redundant_count += 1
    elif elf_2[0] <= elf_1[0] and elf_2[1] >= elf_1[1]:
        redundant_count += 1

print(redundant_count)