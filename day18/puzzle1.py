"""
Day 18 - Puzzle 1: [Puzzle Title]

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
    counter = 0
    counter_limit = 1024 # 12 for sample, 1024 for input

    for line in lines:
        my_coordinate = line.split(',')
        coordinates.append((int(my_coordinate[0]), int(my_coordinate[1])))
        counter += 1
        if counter >= counter_limit:
            break

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
    visited = set()
    positions = [(0,0)]
    corrupted_mem = data["corrupted_mem"]
    steps = 0

    not_arrived = 1

    while not_arrived:
        steps += 1
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
                    break
                elif (my_new_x,my_new_y) not in corrupted_mem:
                    visited.add((my_new_x,my_new_y))
                    new_positions.append((my_new_x, my_new_y))

            # check left
            my_new_x = my_x - 1
            my_new_y = my_y
            if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                if my_new_x == my_new_y == boundary:
                    not_arrived = 0
                    break
                elif (my_new_x,my_new_y) not in corrupted_mem:
                    visited.add((my_new_x,my_new_y))
                    new_positions.append((my_new_x, my_new_y))

            # check up
            my_new_x = my_x
            my_new_y = my_y - 1
            if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                if my_new_x == my_new_y == boundary:
                    not_arrived = 0
                    break
                elif (my_new_x,my_new_y) not in corrupted_mem:
                    visited.add((my_new_x,my_new_y))
                    new_positions.append((my_new_x, my_new_y))

            # check down
            my_new_x = my_x
            my_new_y = my_y + 1
            if check_in_limit(my_new_x, my_new_y, boundary) and (my_new_x, my_new_y) not in visited:
                if my_new_x == my_new_y == boundary:
                    not_arrived = 0
                    break
                elif (my_new_x,my_new_y) not in corrupted_mem:
                    visited.add((my_new_x,my_new_y))
                    new_positions.append((my_new_x, my_new_y))

        positions = new_positions

    return steps


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
