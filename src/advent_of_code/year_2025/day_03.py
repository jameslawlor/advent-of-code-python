from advent_of_code.utils.input_handling import read_input

def parse_battery_bank_to_ints_list(battery_bank_str):
    return [int(x) for x in battery_bank_str]


def combine_joltages(list_of_joltages):
    return int("".join([str(x) for x in list_of_joltages]))


def calculate_largest_joltage(battery_bank_as_ints):
    largest_joltage_1 = 0
    
    for battery_index, battery_value in enumerate(battery_bank_as_ints):
     if (battery_value > largest_joltage_1) and (battery_index < len(battery_bank_as_ints) - 1):
         largest_joltage_1 = battery_value
         largest_joltage_2 = 0
         for second_battery_value in battery_bank_as_ints[battery_index+1:]:
             if second_battery_value > largest_joltage_2:
                 largest_joltage_2 = second_battery_value
    
    return combine_joltages([largest_joltage_1, largest_joltage_2])


def calculate_largest_joltage_part_2(battery_bank_as_ints, n_batteries=12):
    sorted_batteries = sorted(battery_bank_as_ints, reverse=True)
    return combine_joltages(sorted_batteries[:n_batteries])


def solve_part(input, part=1):
    joltage_list = []

    if part == 1:
        calculate_largest_joltage_function = calculate_largest_joltage
    elif part == 2:
        calculate_largest_joltage_function = calculate_largest_joltage_part_2
    else:
        raise ValueError("Part must be 1 or 2")
    
    for battery_bank_str in input:
        battery_bank_as_ints = parse_battery_bank_to_ints_list(battery_bank_str)
        largest_joltage = calculate_largest_joltage_function(battery_bank_as_ints)
        joltage_list.append(largest_joltage)

    return sum(joltage_list)

def solve(input):
    part_1_solution = solve_part(input, part=1)
    part_2_solution = solve_part(input, part=2)
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
