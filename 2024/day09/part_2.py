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


# Defrag
def next_free_space(disk, offset=0):
    try:
        space_start = disk.index(".")
    except ValueError:
        return [False, False, False]
    space_end = space_start + 1
    try:
        while disk[space_end] == ".":
            space_end += 1
    except IndexError:
        pass
    space_size = space_end - space_start
    return space_start + offset, space_end + offset, space_size


for file_id in range(file_id - 1, 1, -1):
    print(f"Attempting to move: {file_id}... ", end="")
    file_size = disk.count(file_id)
    disk_to_check = disk[:disk.index(file_id)]
    space_start, space_end, space_size = next_free_space(disk_to_check)
    if not space_size:
        print("Failed")
    while space_size:
        if file_size <= space_size:
            pos_add = space_start
            pos_del = disk.index(file_id)
            for _ in range(file_size):
                disk[pos_add] = file_id
                disk[pos_del] = "."
                pos_add += 1
                pos_del += 1
            print("Success")
            break
        else:
            disk_to_check = disk[space_end:disk.index(file_id)]
            space_start, space_end, space_size = next_free_space(disk_to_check, space_end)

# Calculate checksum
checksum = 0
for pos, val in enumerate(disk):
    if val != ".":
        checksum += pos * val

print(checksum)
