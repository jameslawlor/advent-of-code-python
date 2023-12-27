from aoc_2023.solvers.day_3_solvers import (
    get_symbol_positions,
    identify_part_numbers,
    calculate_sum_of_part_numbers,
    solve_day_3,
)
from aoc_2023.utils.input_handling import read_input, parse_args


def main():
    args = parse_args()
    input = read_input(args.input_file)
    result = solve_day_3(input)
    print(f"Day 3: The sum of part numbers is {result}")


if __name__ == "__main__":
    main()
