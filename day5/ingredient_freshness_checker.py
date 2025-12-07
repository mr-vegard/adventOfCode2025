from dataclasses import dataclass

@dataclass
class IDRange():
    start: int
    stop: int

@dataclass
class Ingredient():
    id: int
    fresh: bool



with open("input.txt", "r") as f:
    input_list = f.readlines()


ids_ranges: list[IDRange] = []
ingredients: list[Ingredient] = []

for line in input_list:
    line = line.strip().replace("\n", "").replace("\r", "")
    if "-" in line:
        ids_ranges.append(
            IDRange(
                start=int(line.split("-")[0]), 
                stop=int(line.split("-")[1]))
            )
    elif line.isnumeric():
        ingredients.append(
            Ingredient(
                id=int(line),
                fresh=False
            )
        )

for ingredient in ingredients:
    for range_ in ids_ranges:
        if range_.start <= ingredient.id <= range_.stop:
            ingredient.fresh = True


fresh_counter = 0
for ingredient in ingredients:
    fresh_counter += 1 if ingredient.fresh else 0

print(fresh_counter)
