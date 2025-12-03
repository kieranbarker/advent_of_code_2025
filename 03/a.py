from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
banks = contents.splitlines()
total = 0

for bank in banks:
    largest = 0
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > largest:
                largest = joltage
    total += largest

print(total)
