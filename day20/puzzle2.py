"""
Day 20 - Puzzle 2: [Puzzle Title]

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

def radius(my_pos, my_range, max_x, max_y):
    my_x, my_y = my_pos
    reply = []

    for x in range(my_x-my_range, my_x+my_range+1):
        if 0<= x < max_x:
            for y in range(my_y-my_range, my_y+my_range+1):
                if 0 <= y < max_y:
                    dist = abs(x - my_x) + abs(y - my_y)
                    if dist <= my_range and dist != 0:
                        reply.append((x,y,dist))
    return reply

def try_to_cheat(my_pos, my_map, max_x, max_y, my_range):
    cheat_pos = []

    for new_pos in radius(my_pos, my_range, max_x, max_y):
        my_new_pos = new_pos[0], new_pos[1]
        my_new_dist = new_pos[2]
        if my_map[my_new_pos] == '.' or my_map[my_new_pos] == 'E':
            cheat_pos.append((my_new_pos, my_new_dist))

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
    my_range = 20

    for pos in my_racetrack:
        for cheated_pos_dist in try_to_cheat(pos, data["map"], data["max_x"], data["max_y"], my_range):
            cheated_pos = cheated_pos_dist[0]
            cheated_dist = cheated_pos_dist[1]
            saved_time = my_racetrack[cheated_pos] - my_racetrack[pos] - cheated_dist
            if saved_time > 0:
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
