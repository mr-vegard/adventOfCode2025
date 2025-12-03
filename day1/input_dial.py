from dataclasses import dataclass
from typing import Literal

input_list: list[str] = []

with open("input.txt", "r") as f:
    input_list = f.readlines()


@dataclass
class DialInput():
    direction: Literal["L", "R"]
    value: int

dial_inputs: list[DialInput] = []

for input in input_list:
    dial_inputs.append(DialInput(direction=input[:1], value=int(input[1:])))


def dialer(dial_current: int, zero_counter_current, direction: Literal["L", "R"], dial_input: int):
    for i in range(dial_input):
        del i

        if dial_current == 0:
            zero_counter_current += 1

        if direction == "R":
            if dial_current == 99:
                dial_current -= 100
            dial_current += 1

        if direction == "L":
            if dial_current == 0:
                dial_current += 100
            dial_current -= 1

    return dial_current, zero_counter_current

dial_current: int = 50
zero_counter = 0

for dial_input in dial_inputs:
    dial_current, zero_counter = dialer(dial_current, zero_counter, dial_input.direction, dial_input=dial_input.value)

    print(dial_current)
print(zero_counter)