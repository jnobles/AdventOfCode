with open("puzzle_input") as f:
    puzzle_input = f.readline().strip()

stones = [int(val) for val in puzzle_input.split(" ")]
blinks = 75

from collections import Counter
stone_counts = Counter()
for stone in stones:
    stone_counts.update([stone])

for blink in range(blinks):
    new_counts = Counter()
    while stone_counts:
        stone, count = stone_counts.popitem()
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            a = int(str(stone)[len(str(stone))//2:])
            b = int(str(stone)[:len(str(stone))//2])
            new_counts[a] += count
            new_counts[b] += count
        else:
            new_counts[stone * 2024] += count
    print(f"Blink: {blink + 1} | Stones: {new_counts.total()}")
    stone_counts = +new_counts
