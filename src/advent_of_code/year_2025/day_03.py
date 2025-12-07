from advent_of_code.utils.input_handling import read_input

def parse_battery_bank_to_ints_list(battery_bank_str):
    return [int(x) for x in battery_bank_str]


def combine_joltages(j1, j2):
    return int(f"{j1}{j2}")


def calculate_largest_joltage(battery_bank_as_ints):
    largest_joltage_1 = 0
    

    print(f"Calculating largest joltage for battery bank: {battery_bank_as_ints}")

    for battery_index, battery_value in enumerate(battery_bank_as_ints):
     print(f"battery_value={battery_value}, battery_index={battery_index}")
     if (battery_value > largest_joltage_1) and (battery_index < len(battery_bank_as_ints) - 1):
         largest_joltage_1 = battery_value
         largest_joltage_2 = 0
         print(f"Larger value found! Setting largest_joltage_1 to {largest_joltage_1}")
         for second_battery_value in battery_bank_as_ints[battery_index+1:]:
             print(f"second_battery_value={second_battery_value}")
             if second_battery_value > largest_joltage_2:
                 largest_joltage_2 = second_battery_value
                 print(f"Larger value found! Setting largest_joltage_2 to {largest_joltage_2}")

    print(f"Largest joltage combination: {largest_joltage_1}, {largest_joltage_2}")
    
    return combine_joltages(largest_joltage_1, largest_joltage_2)

def solve_part_1(input):
    joltage_list = []
    for battery_bank_str in input:
        battery_bank_as_ints = parse_battery_bank_to_ints_list(battery_bank_str)
        largest_joltage = calculate_largest_joltage(battery_bank_as_ints)
        joltage_list.append(largest_joltage)

    return sum(joltage_list)

def solve(input):
    part_1_solution = solve_part_1(input)
    part_2_solution = None
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
