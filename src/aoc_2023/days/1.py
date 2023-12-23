import sys

from aoc_2023.helpers import (
    strip_alphabetical_chars_from_string,
    get_first_last_digits_from_string,
    convert_str_to_numerical,
    convert_spelled_numbers_to_numerical,
    read_input,
    parse_args
)

args = parse_args()
input = read_input(args.input_file)

if args.part == "1":
    summation = 0
    for line in input:
        line_numerical_characters_only = strip_alphabetical_chars_from_string(line)
        # print(line, line_numerical_characters_only)
        first_last_digits = get_first_last_digits_from_string(line_numerical_characters_only)
        first_last_digits_int = convert_str_to_numerical(first_last_digits)
        summation += first_last_digits_int
    print(summation)

elif args.part == "2":
    summation = 0
    for line in input:
        convert_spelled_numbers_to_numerical(line)
        result = convert_spelled_numbers_to_numerical(line)
        summation+=result
        # print(line, result)
    print(summation)