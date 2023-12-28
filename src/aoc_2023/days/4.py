from aoc_2023.solvers.day_4_solvers import (
    solve_day_4,
)
from aoc_2023.utils.input_handling import read_input, parse_args


def main():
    args = parse_args()
    input = read_input(args.input_file)
    result_part_1, result_part_2 = solve_day_4(input)
    print(
        f"Day 4: "
        f" Total points for part 1 is {result_part_1}. "
        f" Total points for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
