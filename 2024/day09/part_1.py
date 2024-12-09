with open("puzzle_input") as f:
    puzzle_input = f.readline().strip()

disk_map = [int(val) for val in puzzle_input]
disk = []

# Expand disk map
file_id = 0
while True:
    try:
        file = disk_map.pop(0)
        disk += [file_id for _ in range(file)]
        file_id += 1
    except IndexError:
        break
    try:
        free = disk_map.pop(0)
        disk += ["." for _ in range(free)]
    except IndexError:
        break

# Condense
while "." in disk:
    print(f"Spaces remaining: {disk.count('.')}")
    item = disk.pop()
    if item == ".":
        continue
    disk[disk.index(".")] = item

# Calculate checksum
checksum = 0
for pos, val in enumerate(disk):
    checksum += pos * val

print(checksum)
