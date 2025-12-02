from pathlib import Path
import re

path = Path("input.txt")
contents = path.read_text()
id_ranges = contents.split(",")
total = 0

for id_range in id_ranges:
    start, stop = map(int, id_range.split("-"))
    for id in range(start, stop + 1):
        if re.search(r"^(\d+)\1+$", str(id)):
            total += id

print(total)
