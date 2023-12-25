from aoc_2023.helpers.day_3_solvers import (
    find_schematic_size,
    convert_raw_schematic_to_array,
    find_symbol_indices,
    find_adjacent_numbers,
    identify_part_numbers,
)

def main():
    args = parse_args()
    input = read_input(args.input_file)

    (size_x, size_y) = find_schematic_size(input)
    arr = convert_raw_schematic_to_array(input,size_x,size_y)
    symbol_indices = find_symbol_indices(arr)
    adjacent_number_indices = find_adjacent_numbers(arr, symbol_indices)
    list_of_part_numbers = identify_part_numbers(arr, adjacent_number_indices)
    sum_of_part_numbers = sum(list_of_part_numbers)
    print(f"Day 3: The sum of part numbers is {sum_of_part_numbers}")

if __name__ == "__main__":
    main()
