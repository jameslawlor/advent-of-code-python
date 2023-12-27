import re


class Part:
    def __init__(self, part_number):
        self.part_number = str(part_number)
        self.coordinates = []
        self.window = None

    def set_coordinates(self, y_pos, x_start_pos, x_end_pos):
        if x_start_pos > x_end_pos:
            raise ValueError(
                "Invalid coordinates: "
                "x_start_pos should be less than or equal to x_end_pos"
            )
        self.x_start_coordinate = x_start_pos
        self.x_end_coordinate = x_end_pos
        self.y_coordinate = y_pos
        self.full_coordinates = [(y_pos, x) for x in range(x_start_pos, x_end_pos + 1)]

    def part_number_as_integer(self):
        try:
            return int(self.part_number)
        except (ValueError, TypeError):
            # Handle the case where part_number is not a valid integer
            return None

    def get_window_around_part(self):
        if self.full_coordinates is None:
            raise ValueError(
                "Part has no full_coordinates! Check Part initialised correctly."
            )

        self.window = []
        for y in [self.y_coordinate - 1, self.y_coordinate, self.y_coordinate + 1]:
            for x in range(self.x_start_coordinate - 1, self.x_end_coordinate + 1):
                self.window.append((y, x))

    def check_window_for_symbol(self, symbol_coordinates):
        return bool(set(self.window).intersection(symbol_coordinates))


class Symbol:
    def __init__(self, symbol=None, coordinates=None):
        self.symbol = symbol
        self.coordinates = coordinates
        self.is_gear = False

    def set_coordinates(self, y_pos, x_pos):
        self.coordinates = (y_pos, x_pos)

    def set_symbol(self, char):
        self.symbol = char
        self.is_potential_gear = self.symbol == "*"

    def mark_as_gear(self):
        self.is_gear = True


def check_char_is_number(char) -> bool:
    return bool(re.search(r"\d", char))


def check_char_is_symbol(char) -> bool:
    return bool(re.search(r"[^.\d]", char))


def get_symbols(input) -> set:
    symbols_list = []
    for line_number, line in enumerate(input):
        for x_pos, char in enumerate(line):
            if check_char_is_symbol(char):
                sym = Symbol()
                sym.set_coordinates(line_number, x_pos)
                sym.set_symbol(char)
                symbols_list.append(sym)
    return symbols_list


def check_window_for_symbol(window, symbol_positions) -> bool:
    return bool(window.intersection(symbol_positions))


def identify_part_numbers(input, symbols_collection) -> list:
    parts_list = []

    symbol_positions = [s.coordinates for s in symbols_collection]

    for line_number, line in enumerate(input):
        matched_numbers = re.finditer("(\\d+)", line)
        for match in matched_numbers:
            match_start = match.start()
            match_end = match.end()
            part_number = match.group()
            part = Part(
                part_number=part_number,
            )
            part.set_coordinates(line_number, match_start, match_end)
            part.get_window_around_part()
            if part.check_window_for_symbol(symbol_positions):
                parts_list.append(part)

    return parts_list


def identify_gears(parts_collection, symbol_collection):
    # for sym in symbol_collection:
    # get window around symbol

    #

    return


def calculate_sum_of_part_numbers(input_list) -> int:
    return sum([part.part_number_as_integer() for part in input_list])


def solve_day_3(input) -> int:
    symbol_collection = get_symbols(input)
    parts_collection = identify_part_numbers(input, symbol_collection)
    sum_of_part_numbers = calculate_sum_of_part_numbers(parts_collection)
    # gears_collection = identify_gears(parts_collection, symbol_collection)
    # sum_of_gear_ratios = calculate_sum_of_gear_ratios()
    return sum_of_part_numbers
