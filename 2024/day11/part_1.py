with open("puzzle_input") as f:
    puzzle_input = f.readline().strip()

stones = [int(val) for val in puzzle_input.split(" ")]
blinks = 25

for blink in range(blinks):
    old_stones = stones
    stones = []
    while old_stones:
        stone = old_stones.pop(0)
        if stone == 0:
            stones.append(1)
        elif len(str(stone)) % 2 == 0:
            digits = len(str(stone))
            half_len = int(digits/2)
            stones.append(int(str(stone)[:half_len]))
            stones.append(int(str(stone)[half_len:]))
        else:
            stones.append(stone * 2024)
    print(stones)
