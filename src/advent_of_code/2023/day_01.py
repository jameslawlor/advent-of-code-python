from advent_of_code.utils.input_handling import (
    read_input,
    parse_args,
)

import re

SPELLED_NUMBERS_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_patterns(accept_written_digits) -> list:
    numerics_as_strings = [str(x) for x in range(1, 10)]

    if not accept_written_digits:
        patterns_to_return = numerics_as_strings
    else:
        spelled_numbers_list = list(SPELLED_NUMBERS_MAPPING.keys())
        patterns_to_return = numerics_as_strings + spelled_numbers_list

    return patterns_to_return


def convert_str_to_numerical(input_string):
    return int(input_string)


def solve_all_calibration_values(input, patterns_to_find) -> int:
    sum_of_calibration_values = 0
    for line in input:
        calibration_value = solve_single_calibration_value(line, patterns_to_find)
        sum_of_calibration_values += calibration_value
    return sum_of_calibration_values


def solve_single_calibration_value(line, patterns_to_find) -> int:
    patterns_and_their_indices = find_indices_of_patterns(line, patterns_to_find)
    (first_pattern_str, last_pattern_str) = find_first_and_last_patterns(
        patterns_and_their_indices
    )
    calibration_value = convert_first_last_patterns_to_calibration_value(
        first_pattern_str, last_pattern_str
    )
    return calibration_value


def find_first_and_last_patterns(patterns_and_their_indices):
    # find highest and lowest indices
    lowest_index = None
    highest_index = None
    char_at_lowest = ""
    char_at_highest = ""
    for pattern, indices in patterns_and_their_indices.items():
        if indices:
            tmp_lowest_index = min(indices)
            tmp_highest_index = max(indices)

            if lowest_index is None or tmp_lowest_index < lowest_index:
                lowest_index = tmp_lowest_index
                char_at_lowest = pattern

            if highest_index is None or tmp_highest_index > highest_index:
                highest_index = tmp_highest_index
                char_at_highest = pattern

    return (char_at_lowest, char_at_highest)


def convert_first_last_patterns_to_calibration_value(
    first_pattern_str, last_pattern_str
):
    if first_pattern_str in SPELLED_NUMBERS_MAPPING.keys():
        first_pattern_str = str(SPELLED_NUMBERS_MAPPING[first_pattern_str])

    if last_pattern_str in SPELLED_NUMBERS_MAPPING.keys():
        last_pattern_str = str(SPELLED_NUMBERS_MAPPING[last_pattern_str])

    return int(first_pattern_str + last_pattern_str)


def find_indices_of_patterns(line, patterns_to_find):
    patterns_and_indices = {p: [] for p in patterns_to_find}

    for pattern in patterns_to_find:
        matches = re.finditer(pattern, line)
        patterns_and_indices[pattern] = [m.start() for m in matches]

    return patterns_and_indices

def main():
    args = parse_args()
    input = read_input(args.input_file)

    if args.part == 1:
        accept_written_digits = False
    elif args.part == 2:
        accept_written_digits = True

    patterns_to_find = get_patterns(accept_written_digits)
    calibration_value_sum = solve_all_calibration_values(input, patterns_to_find)
    print(
        f"Day 1: Solution with accept_written_digits={accept_written_digits}"
        f" is {calibration_value_sum}."
    )


if __name__ == "__main__":
    main()
