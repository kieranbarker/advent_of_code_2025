from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
fresh_ingredients, available_ingredients = contents.split("\n\n")

fresh_ingredients = fresh_ingredients.splitlines()

fresh_ingredients = [
    ingredient_range.split("-") for ingredient_range in fresh_ingredients
]

fresh_ingredients = [
    range(int(start), int(stop) + 1) for start, stop in fresh_ingredients
]

available_ingredients = map(int, available_ingredients.splitlines())

total = 0

for ingredient in available_ingredients:
    for ingredient_range in fresh_ingredients:
        if ingredient in ingredient_range:
            total += 1
            break

print(total)
