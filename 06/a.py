from pathlib import Path
from re import split
from math import prod


def solve(column):
    operator = column[-1]
    operands = map(int, column[:-1])

    if operator == "+":
        result = sum(operands)
    elif operator == "*":
        result = prod(operands)

    return result


path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()
grid = [split(r"\s+", line.strip()) for line in lines]
columns = [list(col) for col in zip(*grid)]
total = sum(map(solve, columns))
print(total)
