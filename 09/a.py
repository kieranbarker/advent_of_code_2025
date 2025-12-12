from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()
red_tiles = [(i, j) for j, i in (map(int, line.split(",")) for line in lines)]
largest = 0

for i, j in red_tiles:
    for k, l in red_tiles:
        rows = abs(i - k) + 1
        cols = abs(j - l) + 1
        area = rows * cols
        if area > largest:
            largest = area

print(largest)
