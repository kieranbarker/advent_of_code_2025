from pathlib import Path


def get_adjacent_positions(i, j):
    return [
        (i + di, j + dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0)
    ]


def is_valid_position(position, grid):
    return position[0] in range(len(grid)) and position[1] in range(len(grid[0]))


def find_accessible_rolls(grid):
    accessible_rolls = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue

            adjacent_rolls = 0
            adjacent_positions = get_adjacent_positions(i, j)

            valid_positions = [
                position
                for position in adjacent_positions
                if is_valid_position(position, grid)
            ]

            for k, l in valid_positions:
                if grid[k][l] == "@":
                    adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessible_rolls.append((i, j))

    return accessible_rolls


path = Path("input.txt")
contents = path.read_text()
grid = [list(line) for line in contents.splitlines()]
accessible_rolls = find_accessible_rolls(grid)
removed_rolls = 0

while accessible_rolls:
    for i, j in accessible_rolls:
        grid[i][j] = "x"
        removed_rolls += 1
    accessible_rolls = find_accessible_rolls(grid)

print(removed_rolls)
