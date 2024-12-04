import re

with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]
    puzzle_input = ''.join(puzzle_input)

mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

result = 0
puzzle_input = re.sub(r"don't\(\).*?do\(\)", "", puzzle_input)
puzzle_input = re.sub(r"don't\(\).*", "", puzzle_input)
matches = mul_pattern.findall(puzzle_input)
for x, y in matches:
    result += int(x) * int(y)

print(result)
