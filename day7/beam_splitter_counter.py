
with open("input.txt", "r") as f:
    input_list = f.readlines()


ser_input_list = []

for row in input_list:
    ser_input_list.append(list(row.replace("\n", "").strip()))


beam_tree = ser_input_list
beam_indexes = set()
Beam_split_counter = 0

for line_index, line in enumerate(ser_input_list):
    for i, symbol in enumerate(line):
        if symbol == "S":
            beam_indexes.add(i)
        if i in beam_indexes and symbol == "^":
            beam_indexes.add(i+1)
            beam_indexes.add(i-1)

            beam_tree[line_index][i-1] = "|"
            beam_tree[line_index][i+1] = "|"

            beam_indexes.remove(i) if i in beam_indexes else None
            Beam_split_counter += 1

        if i in beam_indexes and symbol == ".":
            beam_tree[line_index][i] = "|"
    rebuild_string = ""


rebuild_string = ""
for line in beam_tree:
    rebuild_string += "".join(line)

print(rebuild_string)
print(f"The beam has been split: {Beam_split_counter} times")