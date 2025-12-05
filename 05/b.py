from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
fresh_ingredients, _ = contents.split("\n\n")

fresh_ingredients = fresh_ingredients.splitlines()

fresh_ingredients = [
    ingredient_range.split("-") for ingredient_range in fresh_ingredients
]

fresh_ingredients = [
    range(int(start), int(stop) + 1) for start, stop in fresh_ingredients
]

fresh_ingredients.sort(key=lambda ingredient_range: ingredient_range[0])

merged_ranges = fresh_ingredients[:1]

for ingredient_range in fresh_ingredients[1:]:
    if merged_ranges[-1][-1] >= ingredient_range[0]:
        start = merged_ranges[-1][0]
        stop = max(merged_ranges[-1][-1], ingredient_range[-1]) + 1
        merged_ranges[-1] = range(start, stop)
    else:
        merged_ranges.append(ingredient_range)

total = sum(len(merged_range) for merged_range in merged_ranges)
print(total)
