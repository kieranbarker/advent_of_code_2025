from pathlib import Path
from math import prod


def split_by_empty_columns(grid):
    rows = len(grid)
    cols = len(grid[0])

    # determine which columns are separators (all rows are ' ')
    is_sep = [all(grid[r][c] == " " for r in range(rows)) for c in range(cols)]

    results = []
    start = None

    for c in range(cols):
        if not is_sep[c]:
            if start is None:
                start = c
        else:
            if start is not None:
                # slice columns start..c-1
                results.append(
                    [[grid[r][k] for k in range(start, c)] for r in range(rows)]
                )
                start = None

    if start is not None:
        results.append([[grid[r][k] for k in range(start, cols)] for r in range(rows)])

    return results


def solve(problem):
    columns = [list(col) for col in zip(*problem)]
    operator = columns[0][-1]
    operands = [columns[0][:-1]] + columns[1:]
    operands = [int("".join(operand)) for operand in operands]

    if operator == "+":
        result = sum(operands)
    elif operator == "*":
        result = prod(operands)

    return result


path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()
grid = [list(line) for line in lines]
problems = split_by_empty_columns(grid)
total = sum(map(solve, problems))
print(total)
