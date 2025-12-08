"""
Day 16 - Puzzle 2: [Puzzle Title]

[Brief description of the puzzle]
"""
from time import process_time_ns


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

    my_map = {}
    my_raw=0

    for line in lines:
        for inc in range(0, len(line)):
            if line[inc] == 'E':
                my_end = (my_raw, inc)
            elif line[inc] == 'S':
                my_start = (my_raw, inc)
            my_map[my_raw,inc] = line[inc]
        my_raw += 1

    return {"map": my_map, "start": my_start, "end": my_end}


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

    result = -1
    positions = {(data['start'],'E',(data['start'],)):0}
    my_end = data['end']
    maze = data['map']

    best_paths = []

    visited_positions = {(data['start'],'E'):0}

    while positions and (result == -1 or result > min(positions.values())):
        new_positions = {}
        for key in positions.keys():
            position = key[0]
            direction = key[1]

            #check move
            new_direction = direction
            new_score = positions[key] + 1
            new_history = list(key[2]).copy()

            if direction == 'E':
                new_position = (position[0], position[1]+1)
            elif direction == 'S':
                new_position = (position[0]+1, position[1])
            elif direction == 'W':
                new_position = (position[0], position[1]-1)
            else: # 'N'
                new_position = (position[0]-1, position[1])
            new_history.append(new_position)

            if (maze[new_position] != '#') and \
                    (((new_position, new_direction) not in visited_positions) or \
                     (new_score <= visited_positions[(new_position, new_direction)])):
                visited_positions[(new_position, new_direction)] = new_score
                if new_position == my_end:
                    if (result == -1) or (new_score <= result):
                        if result == new_score:
                            best_paths.append(new_history)
                        else:
                            best_paths = [new_history]
                        result = new_score
                else:
                    new_positions[(new_position, new_direction, tuple(new_history))] = new_score

            # check clockwise
            new_position = position
            new_score = positions[key] + 1000
            new_history = list(key[2]).copy()

            if direction == 'E':
                new_direction = 'S'
            elif direction == 'S':
                new_direction = 'W'
            elif direction == 'W':
                new_direction = 'N'
            else: # 'N'
                new_direction = 'E'

            if ((new_position, new_direction) not in visited_positions) or \
                    new_score <= visited_positions[(new_position, new_direction)]:
                visited_positions[(new_position, new_direction)] = new_score
                new_positions[(new_position, new_direction, tuple(new_history))] = new_score

            # check counterclockwise
            new_position = position
            new_score = positions[key] + 1000
            new_history = list(key[2]).copy()

            if direction == 'E':
                new_direction = 'N'
            elif direction == 'S':
                new_direction = 'E'
            elif direction == 'W':
                new_direction = 'S'
            else:  # 'N'
                new_direction = 'W'

            if ((new_position, new_direction) not in visited_positions) or \
                    new_score <= visited_positions[(new_position, new_direction)]:
                visited_positions[(new_position, new_direction)] = new_score
                new_positions[(new_position, new_direction, tuple(new_history))] = new_score

        positions = new_positions

    best_positions = set()
    for path in best_paths:
        for pos in path:
            best_positions.add(pos)
    return len(best_positions)


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
