"""
Day 18 - Puzzle 2: [Puzzle Title]

[Brief description of the puzzle]
"""

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
    coordinates = []

    for line in lines:
        my_coordinate = line.split(',')
        coordinates.append((int(my_coordinate[0]), int(my_coordinate[1])))

    return {"corrupted_mem": coordinates}

def check_in_limit(x, y,  limit):
    return 0 <= x <= limit and 0 <= y <= limit

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

    boundary = 70 # 6 for sample, 70 for input
    byte_index = 1024 # start at 12 for sample, 1024 for input

    not_blocked = 1

    while not_blocked:
        not_arrived = 1
        positions = [(0, 0)]
        corrupted_mem = data["corrupted_mem"][:byte_index]
        visited = set()

        print(byte_index)

        while not_arrived and positions:
            new_positions = []
            for position in positions:
                my_x = position[0]
                my_y = position[1]

                # check right
                my_new_x = my_x + 1
                my_new_y = my_y
                if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                    if my_new_x == my_new_y == boundary:
                        not_arrived = 0
                    elif (my_new_x,my_new_y) not in corrupted_mem:
                        visited.add((my_new_x,my_new_y))
                        new_positions.append((my_new_x, my_new_y))

                # check left
                my_new_x = my_x - 1
                my_new_y = my_y
                if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                    if my_new_x == my_new_y == boundary:
                        not_arrived = 0
                    elif (my_new_x,my_new_y) not in corrupted_mem:
                        visited.add((my_new_x,my_new_y))
                        new_positions.append((my_new_x, my_new_y))

                # check up
                my_new_x = my_x
                my_new_y = my_y - 1
                if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                    if my_new_x == my_new_y == boundary:
                        not_arrived = 0
                    elif (my_new_x,my_new_y) not in corrupted_mem:
                        visited.add((my_new_x,my_new_y))
                        new_positions.append((my_new_x, my_new_y))

                # check down
                my_new_x = my_x
                my_new_y = my_y + 1
                if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                    if my_new_x == my_new_y == boundary:
                        not_arrived = 0
                    elif (my_new_x,my_new_y) not in corrupted_mem:
                        visited.add((my_new_x,my_new_y))
                        new_positions.append((my_new_x, my_new_y))

            positions = new_positions

        if not_arrived == 1:
            not_blocked = 0
        else:
            byte_index += 1

    return data["corrupted_mem"][byte_index-1]


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = None  # Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
