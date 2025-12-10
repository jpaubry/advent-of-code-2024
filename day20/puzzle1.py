"""
Day 20 - Puzzle 1: [Puzzle Title]

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

    map={}
    raw = 0
    for line in lines:
        for ind in range(0, len(line)):
            map[(raw,ind)] = line[ind]
            if line[ind] == 'S':
                start = (raw, ind)
            if line[ind] == 'E':
                end = (raw, ind)
        raw += 1

    return {"map": map, "start": start, "end": end, "max_x": raw - 1, "max_y": len(lines[0])}

def next_pos(my_pos, prev_pos, my_map):
    my_x, my_y = my_pos

    my_new_pos = my_x, my_y + 1 # look right
    if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
        if my_new_pos != prev_pos:
            return my_new_pos

    my_new_pos = my_x + 1, my_y # look down
    if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
        if my_new_pos != prev_pos:
            return my_new_pos

    my_new_pos = my_x, my_y - 1 # look left
    if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
        if my_new_pos != prev_pos:
            return my_new_pos

    my_new_pos = my_x - 1, my_y # look up
    if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
        if my_new_pos != prev_pos:
            return my_new_pos

def try_to_cheat(my_pos, my_map, max_x, max_y):
    cheat_pos = []
    my_x, my_y = my_pos

    my_new_pos = my_x, my_y + 1 # look right
    if my_map[my_new_pos] == '#':
        if my_y + 2 < max_y:
            my_new_pos = my_x, my_y + 2
            if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
                cheat_pos.append(my_new_pos)

    my_new_pos = my_x + 1, my_y # look down
    if my_map[my_new_pos] == '#':
        if my_x + 2 < max_x:
            my_new_pos = my_x + 2, my_y
            if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
                cheat_pos.append(my_new_pos)

    my_new_pos = my_x, my_y - 1 # look left
    if my_map[my_new_pos] == '#':
        if my_y - 2 >= 0:
            my_new_pos = my_x, my_y - 2
            if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
                cheat_pos.append(my_new_pos)

    my_new_pos = my_x - 1, my_y # look up
    if my_map[my_new_pos] == '#':
        if my_x - 2 >= 0:
            my_new_pos = my_x - 2, my_y
            if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
                cheat_pos.append(my_new_pos)

    return cheat_pos

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
    my_previous_pos = data["start"]
    my_current_pos = data["start"]
    timer = 0
    my_racetrack = {my_current_pos: 0}

    while my_current_pos != data["end"]:
        my_new_current_pos = next_pos(my_current_pos, my_previous_pos, data["map"])
        my_previous_pos = my_current_pos
        my_current_pos = my_new_current_pos
        timer += 1
        my_racetrack[my_current_pos] = timer

    print(timer)
    print(len(my_racetrack))

    saved_times = {}
    ordered_saved_times = []

    for pos in my_racetrack:
        for cheated_pos in try_to_cheat(pos, data["map"], data["max_x"], data["max_y"]):
            if my_racetrack[cheated_pos] > my_racetrack[pos]:
                saved_time = my_racetrack[cheated_pos] - my_racetrack[pos] - 2
                if saved_time in saved_times:
                    saved_times[saved_time] += 1
                else:
                    saved_times[saved_time] = 1
                    ordered_saved_times.append(saved_time)

    ordered_saved_times.sort()
    ordered_saved_times.reverse()

    result = 0
    for saved_time in ordered_saved_times:
        print("There are " + str(saved_times[saved_time]) + " cheats that save " + str(saved_time) + " picoseconds.")
        if saved_time >= 100:
            result += saved_times[saved_time]


    return result


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
