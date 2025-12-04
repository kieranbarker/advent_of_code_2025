from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
banks = contents.splitlines()
total = 0

for bank in banks:
    chosen = []
    to_delete = len(bank) - 12

    for i in range(len(bank)):
        while to_delete and chosen and chosen[-1] < bank[i]:
            chosen.pop()
            to_delete -= 1
        chosen.append(bank[i])

    total += int("".join(chosen[:12]))

print(total)
