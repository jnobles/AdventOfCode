import re

with open("puzzle_input") as f:
    puzzle_input = [line.strip() for line in f.readlines()]

mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

result = 0
for line in puzzle_input:
    matches = mul_pattern.findall(line)
    for x, y in matches:
        result += int(x) * int(y)

print(result)
