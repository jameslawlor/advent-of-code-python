from aoc_2023.utils.input_handling import read_input, parse_args
from aoc_2023.solvers.day_2_solvers import solve_day_2


def main():
    args = parse_args()
    input = read_input(args.input_file)
    part_1_solution, part_2_solution = solve_day_2(input)
    print(
        f"Day 2: Part 1 solution is {part_1_solution}."
        f"Part 2 solution is {part_2_solution}."
    )


if __name__ == "__main__":
    main()
