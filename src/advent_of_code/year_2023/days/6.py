from advent_of_code.year_2023.solvers.day_6_solvers import (
    solve_day_6,
)
from advent_of_code.utils.input_handling import read_input, parse_args


def main():
    args = parse_args()
    input = read_input(args.input_file)
    result_part_1, result_part_2 = solve_day_6(input)
    print(
        f"Day 6: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
