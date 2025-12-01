from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()

position = 50
total = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:])

    for _ in range(distance):
        if direction == "L":
            position = (position - 1) % 100
        elif direction == "R":
            position = (position + 1) % 100

        if position == 0:
            total += 1

print(total)
