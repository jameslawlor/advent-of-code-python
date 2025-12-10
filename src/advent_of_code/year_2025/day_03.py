from advent_of_code.utils.input_handling import read_input


def parse_battery_bank_to_ints_list(battery_bank_str):
    return [int(x) for x in battery_bank_str]


def combine_joltages(list_of_joltages):
    return int("".join([str(x) for x in list_of_joltages]))


def find_max_and_leftmost_index(input_list):
    max_value = max(input_list)
    leftmost_index = input_list.index(max_value)
    return max_value, leftmost_index


def calculate_largest_joltage(battery_bank_as_ints, n_batteries):

    batteries_remaining = n_batteries
    bank_len = len(battery_bank_as_ints)
    list_of_joltages = []
    start_ix = 0

    while batteries_remaining > 0:
        end_ix = bank_len - batteries_remaining + 1
        window_to_check = battery_bank_as_ints[start_ix:end_ix]

        # find largest value in window and the left-most index for dupes
        max_value, leftmost_index_window = find_max_and_leftmost_index(window_to_check)
        leftmost_index = leftmost_index_window + start_ix
        list_of_joltages.append(max_value)

        # reassign start_ix and update remaining batteries
        start_ix = leftmost_index + 1
        batteries_remaining -= 1

    return combine_joltages(list_of_joltages)


def solve_part(input, n_batteries):
    joltage_list = []

    for battery_bank_str in input:
        battery_bank_as_ints = parse_battery_bank_to_ints_list(battery_bank_str)
        largest_joltage = calculate_largest_joltage(battery_bank_as_ints, n_batteries)
        joltage_list.append(largest_joltage)

    return sum(joltage_list)


def solve(input):
    part_1_solution = solve_part(input, n_batteries=2)
    part_2_solution = solve_part(input, n_batteries=12)
    return (part_1_solution, part_2_solution)


def main(input_file):
    input = read_input(input_file)
    (result_part_1, result_part_2) = solve(input)
    print(
        f"Day 01 \n"
        f" Result for part 1 is {result_part_1} \n"
        f" Result for part 2 is {result_part_2} \n"
    )


if __name__ == "__main__":
    main()
