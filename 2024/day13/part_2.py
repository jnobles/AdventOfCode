import fractions
import re

with open("puzzle_input") as f:
    puzzle_input = f.read()

cost = 0
offset = 10000000000000
for match in re.finditer(r"Button A: X\+(?P<a1>\d+), Y\+(?P<a2>\d+)\nButton B: X\+(?P<b1>\d+), Y\+(?P<b2>\d+)\nPrize: X=(?P<x>\d+), Y=(?P<y>\d+)", puzzle_input):
    a1 = int(match.group("a1"))
    a2 = int(match.group("a2"))
    b1 = int(match.group("b1"))
    b2 = int(match.group("b2"))
    x = int(match.group("x")) + offset
    y = int(match.group("y")) + offset
    b = fractions.Fraction(y*a1-a2*x, a2) * fractions.Fraction(a2, a1*b2-a2*b1)
    a = fractions.Fraction(x-b1*b, a1)
    if a.denominator == 1 and b.denominator == 1:
        cost += int(3 * a + b)
    else:
        pass
print(cost)

# Generalized A-press solution (when B is known)
# (x-b1B)/a1

# Generalized B-press solution
# ((ya1-a2x)/a2)(a2/(a1b2-a2b1))


