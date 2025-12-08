from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()

start = (0, lines[0].index("S"))
stack = [start]
visited = set([start])
splits = 0

while stack:
    row, col = stack.pop()
    row += 1

    if not (0 <= row < len(lines)):
        continue

    if lines[row][col] == "^":
        splits += 1

        for new_col in (col - 1, col + 1):
            new_beam = (row, new_col)

            if new_beam not in visited:
                visited.add(new_beam)
                stack.append(new_beam)
    else:
        new_beam = (row, col)

        if new_beam not in visited:
            visited.add(new_beam)
            stack.append(new_beam)

print(splits)
