from pathlib import Path


def get_adjacent_positions(i, j):
    return [
        (i + di, j + dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0)
    ]


def is_valid_position(position, grid):
    return position[0] in range(len(grid)) and position[1] in range(len(grid[0]))


path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()
accessible_rolls = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != "@":
            continue

        adjacent_rolls = 0
        adjacent_positions = get_adjacent_positions(i, j)

        valid_positions = [
            position
            for position in adjacent_positions
            if is_valid_position(position, lines)
        ]

        for k, l in valid_positions:
            if lines[k][l] == "@":
                adjacent_rolls += 1

        if adjacent_rolls < 4:
            accessible_rolls += 1

print(accessible_rolls)
