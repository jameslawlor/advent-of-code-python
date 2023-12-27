from aoc_2023.solvers.day_5_solvers import (
    solve_day_5,
)
from aoc_2023.utils.input_handling import read_input, parse_args

def main():
    args = parse_args()
    input = read_input(args.input_file)
    result_part_1 = solve_day_5(input)
    print(
        f"Day 5: "
        f" Total points for part 1 is {result_part_1}. "
    )


if __name__ == "__main__":
    main()
