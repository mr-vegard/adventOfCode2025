from dataclasses import dataclass

@dataclass
class IDRange():
    start: int
    stop: int

input_list: list[str] = []

with open("input.txt", "r") as f:
    input_list = f.read().split(",")

id_list: list[IDRange] = []

for id in input_list:
    id_list.append(IDRange(start=int(id.split("-")[0]), stop=int(id.split("-")[1])))

def split_id_in_half(id: int) -> int:
    id_string = str(id)
    first_id_half = id_string[:int(len(id_string)/2)]
    last_id_half = id_string[int(len(id_string)/2):]

    if first_id_half == last_id_half:
        return id
    return 0

invalid_ids_sum = 0

for id in id_list:
    for i in range(id.start, id.stop):
        invalid_ids_sum += split_id_in_half(i)

print(invalid_ids_sum)