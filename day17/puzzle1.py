"""
Day 17 - Puzzle 1: [Puzzle Title]

[Brief description of the puzzle]
"""

import re
from unittest import case


def parse_input(input_data: str):
    """
    Parse the input data into a usable format.

    Args:
        input_data: Raw input string from file

    Returns:
        Parsed data structure (list, dict, etc.)
    """
    lines = input_data.strip().split('\n')

    # Implement parsing logic
    my_register_a = 0
    my_register_b = 0
    my_register_c = 0
    my_program = []

    for line in lines:
        match = re.match(r'^(.+):\s(.+)$', line)

        if match:
            my_key = match.group(1)
            my_value = match.group(2)

            if my_key == "Register A":
                my_register_a = int(my_value)
            elif my_key == "Register B":
                my_register_b = int(my_value)
            elif my_key == "Register C":
                my_register_c = int(my_value)
            else:
                for prog in my_value.split(','):
                    my_program.append(int(prog))

    return {"registerA": my_register_a, "registerB": my_register_b, "registerC": my_register_c, "program": my_program}


    return lines


class Computer:
    def __init__(self, registerA, registerB, registerC, program):
        self.registerA = registerA
        self.registerB = registerB
        self.registerC = registerC
        self.program = program
        self.pointer = 0
        self.output = []

    def combo(self, operand):
        if operand == 0:
            return 0
        elif operand == 1:
            return 1
        elif operand == 2:
            return 2
        elif operand == 3:
            return 3
        elif operand == 4:
            return self.registerA
        elif operand == 5:
            return self.registerB
        elif operand == 6:
            return self.registerC
        else:
            return 7

    def state(self):
        print("Register A: {}".format(self.registerA))
        print("Register B: {}".format(self.registerB))
        print("Register C: {}".format(self.registerC))

    def operation(self):
        opcode = self.program[self.pointer]
        operand = self.program[self.pointer + 1]
        if opcode == 0:
            self.adv(operand)
        elif opcode == 1:
            self.bxl(operand)
        elif opcode == 2:
            self.bst(operand)
        elif opcode == 3:
            self.jnz(operand)
        elif opcode == 4:
            self.bxc(operand)
        elif opcode == 5:
            self.out(operand)
        elif opcode == 6:
            self.bdv(operand)
        else:
            self.cdv(operand)

    def adv(self, operand):
        self.registerA = self.registerA // (2**self.combo(operand))
        self.pointer += 2

    def bxl(self, operand):
        self.registerB = self.registerB ^ operand
        self.pointer += 2

    def bst(self, operand):
        self.registerB = self.combo(operand) % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.registerA != 0:
            if operand < len(self.program):
                self.pointer = operand
            else:
                self.pointer += 2
        else:
            self.pointer += 2

    def bxc(self, operand):
        self.registerB = self.registerB ^ self.registerC
        self.pointer += 2

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.registerB = self.registerA // (2**self.combo(operand))
        self.pointer += 2

    def cdv(self, operand):
        self.registerC = self.registerA // (2**self.combo(operand))
        self.pointer += 2

    def display_output(self):
        return ','.join(map(str, self.output))


def solve(input_data: str):
    """
    Main solution function.

    Args:
        input_data: Raw input string from file

    Returns:
        The puzzle answer
    """
    data = parse_input(input_data)

    # Implement solution logic
    computer = Computer(data["registerA"], data["registerB"], data["registerC"], data["program"])

    while computer.pointer < len(computer.program):
        computer.operation()
        if computer.registerB == computer.registerC == 0:
            print(computer.registerA)

    return computer.display_output()


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  #

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
