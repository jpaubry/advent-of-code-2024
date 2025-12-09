"""
Day 19 - Puzzle 2: [Puzzle Title]

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

    towels = lines[0].split(', ')
    lines.pop(0)
    lines.pop(0)

    patterns = []
    partial_patterns = {}
    max_len = 0

    for line in lines:
        patterns.append(line)
        if len(line) > max_len:
            max_len = len(line)
        for l in range(0, len(line)+1):
            if l not in partial_patterns.keys():
                partial_patterns[l] = []
            if line[:l] not in partial_patterns[l]:
                partial_patterns[l].append(line[:l])

    return {"towels": towels, "patterns": patterns, "partial_patterns": partial_patterns, "max_len": max_len}


def rec_pattern_options(my_design, my_towels, my_encountered):
    if my_design == "":
        return 1
    elif my_design in my_encountered.keys():
        return my_encountered[my_design]
    else:
        reply = 0
        for towel in my_towels:
            len_towel = len(towel)
            if len(my_design) >= len_towel:
                if towel == my_design[-len_towel:]:
                    reply += rec_pattern_options(my_design[:-len_towel], my_towels, my_encountered)
        my_encountered[my_design] = reply
        return reply


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

#    print(data["patterns"])

    possible_designs = []
    for design in data["patterns"]:
        possible_designs.append((design,""))
    validated_designs = set()
    encountered_designs = set()

    while possible_designs:
    #    print(str(min(len(s[0]) for s in possible_designs)) + " " + str(max(len(s[0]) for s in possible_designs)))
    #    print(len(possible_designs))

        new_possible_designs = []
        for design_c in possible_designs:
            design = design_c[0]
            suffix = design_c[1]
            for towel in data["towels"]:
                len_towel = len(towel)
                len_design = len(design)
                if len_towel == len_design:
                    if towel == design:
                        validated_designs.add(design+suffix)
                elif len_towel < len_design:
                    if towel == design[-len_towel:] and (design[:-len_towel],towel+suffix) not in encountered_designs:
                        new_possible_designs.append((design[:-len_towel],towel+suffix))
                        encountered_designs.add((design[:-len_towel],towel+suffix))

        possible_designs = new_possible_designs


    print("Validated designs identified")
    counter = 1
    result = 0
    for design in validated_designs:
        already_encountered = {}
        print(str(counter) + " / " + str(len(validated_designs)))
        result += rec_pattern_options(design, data["towels"], already_encountered)
        counter += 1


    return result


if __name__ == "__main__":
    # Test with sample input
    sample_input = """
    """

    expected_result = 6  # Set expected result from puzzle

    result = solve(sample_input)
    print(f"Sample result: {result}")

    if expected_result is not None:
        assert result == expected_result, f"Expected {expected_result}, got {result}"
        print("✓ Sample test passed!")
