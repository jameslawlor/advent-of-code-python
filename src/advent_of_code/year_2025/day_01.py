from advent_of_code.utils.input_handling import read_input

DIAL_STARTING_POSITION = 50
DIAL_START = 0
DIAL_END = 99

def parse_instruction(instruction):
    turn_direction = instruction[0]
    if turn_direction == "L":
        turn_direction = -1
    elif turn_direction == "R":
        turn_direction = 1
    else:
        raise ValueError(f"Invalid turn direction: {turn_direction}")

    distance = int(instruction[1:])
    return (turn_direction, distance)

def turn_dial(current_position, turn_direction, distance):
    return (current_position + turn_direction * distance) % (DIAL_END + 1)

def position_counter(current_position, target_position=0, ):
    if current_position == target_position:
        return 1
    return 0

def solve(parsed_input):

    current_position = DIAL_STARTING_POSITION
    target_position_count = 0
    
    for instruction in parsed_input:
        turn_direction, distance = parse_instruction(instruction)
        current_position = turn_dial(current_position, turn_direction, distance)
        target_position_count += position_counter(current_position)

    part_1_solution = target_position_count
    part_2_solution = None
    return (part_1_solution, part_2_solution)


def main(input_file):
    input = read_input(input_file)
    (result_part_1, result_part_2) = solve(input)
    print(
        f"Day 01: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
