from dataclasses import dataclass



with open("input.txt", "r") as f:
    input_list = f.readlines()


ser_input_list = []

for row in input_list:
    ser_input_list.append(row.replace("\n", "").strip().split())



def row_to_column(list_of_rows: list[list]):
    columns = []
    for i in range(0, len(list_of_rows[0])):
        column = []
        for row in list_of_rows:
            column.append(row[i])
        columns.append(column)
    return columns

def arithmethic_by_input(input):
    operator = input[-1]
    total = 0 if operator == "+" else 1
    for num in input[:-1]:
        num = int(num)
        if operator == "+":
            total += num
        else:
            total *= num
    return total

arithmethic_columns = row_to_column(ser_input_list)
grand_total = 0
for col in arithmethic_columns:
    grand_total += arithmethic_by_input(col)
print(grand_total)