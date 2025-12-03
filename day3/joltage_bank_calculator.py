input_list: list[str] = []

with open("input.txt", "r") as f:
    input_list = f.readlines()

print(input_list)

def find_largest_two_numbers(number: int):
    number_as_string = str(number)
    biggest_first_number = 0
    for i in range(0, len(number_as_string)-1):
        if int(number_as_string[i]) > biggest_first_number:
            biggest_first_number = int(number_as_string[i])
        if biggest_first_number == 9:
            break

    biggest_first_number_position = number_as_string.index(str(biggest_first_number)) + 1
    
    biggest_second_number = 0
    for i in range(biggest_first_number_position, len(number_as_string)):
        if int(number_as_string[i]) > biggest_second_number:
            biggest_second_number = int(number_as_string[i])
    
    return int(str(biggest_first_number)+str(biggest_second_number))


def find_biggest_number(number_as_string):
    biggest_number = 0
    for i in range(0, len(number_as_string)):
        if int(number_as_string[i]) > biggest_number:
            biggest_number = int(number_as_string[i])
        if biggest_number == 9:
            break
    return biggest_number

def find_largest_twelve_number(number:int):
    number_as_string = str(number)

    biggest_number_as_string = ""

    
    
number_total = 0

for number in input_list:
    number_total += find_largest_two_numbers(int(number.strip()))
    print(number_total)
