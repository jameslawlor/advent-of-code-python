from advent_of_code.year_2023.solvers.day_1_solvers import (
    get_patterns,
    solve_all_calibration_values,
)


from advent_of_code.utils.input_handling import (
    read_input,
    parse_args,
)


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
