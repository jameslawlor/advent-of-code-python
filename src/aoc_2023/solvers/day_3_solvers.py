import re


def check_char_is_number(char) -> bool:
    return bool(re.search(r"\d", char))


def check_char_is_symbol(char) -> bool:
    return bool(re.search(r"[^.\d]", char))


def get_symbol_positions(input) -> set:
    symbol_positions = []
    for line_number, line in enumerate(input):
        for x_pos, char in enumerate(line):
            if check_char_is_symbol(char):
                symbol_positions.append((line_number, x_pos))
    return set(symbol_positions)


def get_window(match_start, match_end, line_number) -> set:
    window = []
    for y_pos in [line_number - 1, line_number, line_number + 1]:
        for x_pos in range(match_start - 1, match_end + 1):
            window.append((y_pos, x_pos))
    return set(window)


def check_window_for_symbol(window, symbol_positions) -> bool:
    return bool(window.intersection(symbol_positions))


def identify_part_numbers(input, symbol_positions) -> list:
    part_numbers = []

    for line_number, line in enumerate(input):
        matched_numbers = re.finditer(f"(\\d+)", line)
        line_sum_of_part_numbers = []

        for match in matched_numbers:
            match_start = match.start()
            match_end = match.end()
            part_number = match.group()
            window = get_window(match_start, match_end, line_number)
            if check_window_for_symbol(window, symbol_positions):
                part_numbers.append(part_number)
                line_sum_of_part_numbers.append(part_number)

    return part_numbers


def calculate_sum_of_part_numbers(input_list):
    return sum(list(map(int, input_list)))


def solve_day_3(input):
    symbol_positions = get_symbol_positions(input)
    list_of_part_numbers = identify_part_numbers(input, symbol_positions)
    sum_of_part_numbers = calculate_sum_of_part_numbers(list_of_part_numbers)
    return sum_of_part_numbers
