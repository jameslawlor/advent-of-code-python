import sys

from aoc_2023.helpers.solvers import (
    read_input,
    parse_args,
    get_patterns,
    solve_all_calibration_values,
)


def main():
    args = parse_args()
    input = read_input(args.input_file)
    accept_written_digits = args.accept_written_digits

    patterns_to_find = get_patterns(accept_written_digits)
    calibration_value_sum = solve_all_calibration_values(input, patterns_to_find)
    print(calibration_value_sum)


if __name__ == "__main__":
    main()
