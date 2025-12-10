from advent_of_code.utils.input_handling import read_input

VALID_PARTS = (1, 2)


def parse_input(raw):
    raw_split = raw[0].split(",")
    return raw_split


def convert_range_string_to_pair(range_string):
    range_split = range_string.split("-")
    return (int(range_split[0]), int(range_split[1]))


def split_id(id):
    id_len = len(str(id))
    half_len = id_len // 2
    return (id[:half_len], id[half_len:])


def check_id_valid(id):
    (id_part_1, id_part_2) = split_id(id)
    if id_part_1 == id_part_2:
        return False
    else:
        return True


def check_id_valid_v2(id):
    id_len = len(str(id))
    half_len = id_len // 2
    for sub_str_len in range(1, half_len + 1):
        sub_str = id[:sub_str_len]
        str_to_search = id[sub_str_len:]
        if (
            len(str_to_search) % sub_str_len == 0
        ):  # substr divisible by search str length
            if (
                sub_str * (id_len // sub_str_len) == id
            ):  # substr matches N * search string
                return False
    return True


def get_invalid_ids_in_range(range_pair, part):
    full_range = range(range_pair[0], range_pair[1] + 1)

    if part == 1:
        id_checker_function = check_id_valid
    elif part == 2:
        id_checker_function = check_id_valid_v2
    else:
        raise ValueError("Specify a valid part number")

    invalid_ids = []
    for x in full_range:
        if not id_checker_function(str(x)):
            invalid_ids.append(x)
    return invalid_ids


def find_invalid_ids_in_range_string(range_string, part):
    range_pair_as_ints = convert_range_string_to_pair(range_string)
    invalid_ids_in_range = get_invalid_ids_in_range(range_pair_as_ints, part)
    return invalid_ids_in_range


def find_all_invalid_ids(parsed_input, part):
    invalid_ids = []
    for range_pair in parsed_input:
        invalid_ids.extend(find_invalid_ids_in_range_string(range_pair, part))
    return invalid_ids


def sum_invalid_ids(invalid_ids):
    return sum(invalid_ids)


def solve_part(parsed_input, part):
    invalid_ids = find_all_invalid_ids(parsed_input, part)
    return sum_invalid_ids(invalid_ids)


def solve_part_2(parsed_input):
    invalid_ids = find_all_invalid_ids(parsed_input)
    return sum_invalid_ids(invalid_ids)


def solve(parsed_input):
    part_1_solution = solve_part(parsed_input, part=1)
    part_2_solution = solve_part(parsed_input, part=2)
    return (part_1_solution, part_2_solution)


def main(input_file):
    input = read_input(input_file)
    parsed_input = parse_input(input)
    (result_part_1, result_part_2) = solve(parsed_input)
    print(
        f"Day 01 \n"
        f" Result for part 1 is {result_part_1} \n"
        f" Result for part 2 is {result_part_2} \n"
    )


if __name__ == "__main__":
    main()
