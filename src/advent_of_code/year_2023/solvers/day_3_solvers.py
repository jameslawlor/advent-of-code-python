import re


class Part:
    def __init__(self, part_number):
        self.part_number = str(part_number)
        self.coordinates = []
        self.window = None
        self.x_start_coordinate = None
        self.x_end_coordinate = None
        self.y_coordinate = None
        self.full_coordinates = None

    def __str__(self):
        return (
            "\n"
            f"part_number = {self.part_number} \n"
            f"coordinates = {self.coordinates} \n"
            f"window = {self.window} \n"
            f"x_start_coordinate = {self.x_start_coordinate} \n"
            f"x_end_coordinate = {self.x_end_coordinate} \n"
            f"y_coordinate = {self.y_coordinate} \n"
            f"full_coordinates = {self.full_coordinates} \n"
        )

    def set_coordinates(self, y_pos, x_start_pos, x_end_pos):
        if x_start_pos > x_end_pos:
            raise ValueError(
                "Invalid coordinates: "
                "x_start_pos should be less than or equal to x_end_pos"
            )
        self.x_start_coordinate = x_start_pos
        self.x_end_coordinate = x_end_pos
        self.y_coordinate = y_pos
        self.full_coordinates = [(y_pos, x) for x in range(x_start_pos, x_end_pos)]

        assert len(self.full_coordinates) == len(self.part_number)

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
    def __init__(self, char, y, x):
        self.symbol = char
        self.y = y
        self.x = x
        self.coordinates = (y, x)
        self.is_potential_gear = self.symbol == "*"
        self.is_gear = False
        self.window = None
        self.neighbouring_parts = None
        self.ratio = None

    def __str__(self):
        return (
            "\n"
            f"symbol = {self.symbol} \n"
            f"y = {self.y} \n"
            f"y = {self.x} \n"
            f"x = {self.x} \n"
            f"coordinates = {self.coordinates} \n"
            f"is_potential_gear = {self.is_potential_gear} \n"
            f"is_gear = {self.is_gear} \n"
            f"window = {self.window} \n"
            f"neighbouring_parts = {self.neighbouring_parts} \n"
            f"ratio = {self.ratio} \n"
        )

    def get_surrounding_window(self):
        self.window = []
        for y in [self.y - 1, self.y, self.y + 1]:
            for x in [self.x - 1, self.x, self.x + 1]:
                self.window.append((y, x))

    def check_window_for_parts(self, parts_collection):
        neighbouring_parts = []
        for part in parts_collection:
            coords_to_check = part.full_coordinates
            if bool(set(self.window).intersection(coords_to_check)):
                neighbouring_parts.append(part.part_number)

        self.neighbouring_parts = neighbouring_parts

    def check_if_gear(self):
        if not self.is_potential_gear:
            raise ValueError("Not a potential gear!")

        if len(self.neighbouring_parts) == 2:
            part_numbers_as_int = [int(p) for p in self.neighbouring_parts]
            self.is_gear = True
            self.set_ratio(*part_numbers_as_int)

    def set_ratio(self, n1, n2):
        if not self.is_gear:
            raise ValueError("Ratio can only be set for gears!")

        self.ratio = n1 * n2


def check_char_is_number(char) -> bool:
    return bool(re.search(r"\d", char))


def check_char_is_symbol(char) -> bool:
    return bool(re.search(r"[^.\d]", char))


def get_symbols(input) -> set:
    symbols_list = []
    for line_number, line in enumerate(input):
        for x_pos, char in enumerate(line):
            if check_char_is_symbol(char):
                sym = Symbol(char=char, y=line_number, x=x_pos)
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
    potential_gears_to_check = [
        sym for sym in symbol_collection if sym.is_potential_gear
    ]
    for sym in potential_gears_to_check:
        sym.get_surrounding_window()
        sym.check_window_for_parts(parts_collection)
        sym.check_if_gear()

    gear_collection = [sym for sym in symbol_collection if sym.is_gear]

    return gear_collection


def calculate_sum_of_part_numbers(input_list) -> int:
    return sum([part.part_number_as_integer() for part in input_list])


def calculate_sum_of_gear_ratios(gear_collection) -> int:
    return sum([sym.ratio for sym in gear_collection])


def solve_day_3(input) -> int:
    symbol_collection = get_symbols(input)
    parts_collection = identify_part_numbers(input, symbol_collection)
    sum_of_part_numbers = calculate_sum_of_part_numbers(parts_collection)
    gear_collection = identify_gears(parts_collection, symbol_collection)
    sum_of_gear_ratios = calculate_sum_of_gear_ratios(gear_collection)
    return (sum_of_part_numbers, sum_of_gear_ratios)
