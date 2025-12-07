import pytest

from advent_of_code.year_2023.day_03 import (
    Part,
    Symbol,
    calculate_sum_of_part_numbers,
    check_char_is_number,
    check_char_is_symbol,
    get_symbols,
    identify_gears,
    identify_part_numbers,
    solve_day_3,
)


# Test cases for the Part class
def test_set_coordinates():
    pc = Part(part_number="10")
    pc.set_coordinates(1, 2, 4)
    assert pc.full_coordinates == [
        (1, 2),
        (1, 3),
    ]


def test_set_part_number():
    pc = Part(part_number=123)
    assert pc.part_number == "123"


def test_part_number_as_integer():
    pc = Part(part_number="456")
    # Test conversion when part_number is set
    result = pc.part_number_as_integer()
    assert result == 456

    # Test conversion when part_number is None
    pc.part_number = None
    result = pc.part_number_as_integer()
    assert result is None

    # Test conversion when part_number is not a valid integer string
    pc.part_number = "abc"
    result = pc.part_number_as_integer()
    assert result is None


# Additional test case to demonstrate input validation in set_coordinates
def test_set_coordinates_invalid_input():
    pc = Part(part_number=None)
    with pytest.raises(ValueError, match="Invalid coordinates"):
        pc.set_coordinates(1, 4, 2)


def test_symbol():
    sym = Symbol("$", 1, 2)
    assert sym.symbol == "$"
    assert sym.coordinates == (1, 2)


# Test cases for check_char_is_number function
def test_check_char_is_number_with_number():
    result = check_char_is_number("5")
    assert result is True


def test_check_char_is_number_with_non_number():
    result = check_char_is_number("*")
    assert result is False


def test_check_char_is_number_with_dot():
    result = check_char_is_number(".")
    assert result is False


# Test cases for check_char_is_symbol function
def test_check_char_is_symbol_with_symbol():
    result = check_char_is_symbol("$")
    assert result is True


def test_check_char_is_symbol_with_number():
    result = check_char_is_symbol("7")
    assert result is False


def test_check_char_is_symbol_with_dot():
    result = check_char_is_symbol(".")
    assert result is False


def test_check_char_is_symbol_with_gear():
    result = check_char_is_symbol("*")
    assert result is True


# Additional test case to cover an empty string
def test_check_char_is_symbol_with_empty_string():
    result = check_char_is_symbol("")
    assert result is False


@pytest.fixture
def day_3_test_input():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


@pytest.fixture
def day_3_expected_symbols_collection():
    return [
        Symbol("*", 1, 3),
        Symbol("#", 3, 6),
        Symbol("*", 4, 3),
        Symbol("+", 5, 5),
        Symbol("$", 8, 3),
        Symbol("*", 8, 5),
    ]


@pytest.fixture
def day_3_expected_parts_collection():
    return [
        Part("467"),
        Part("35"),
        Part("633"),
        Part("617"),
        Part("592"),
        Part("755"),
        Part("664"),
        Part("598"),
    ]


def test_get_symbols(day_3_test_input, day_3_expected_symbols_collection):
    test_symbols_list = get_symbols(day_3_test_input)
    output_symbol_positions = [sym.coordinates for sym in test_symbols_list]
    expected_symbol_positions = [
        sym.coordinates for sym in day_3_expected_symbols_collection
    ]
    assert output_symbol_positions == expected_symbol_positions


def test_identify_part_numbers(
    day_3_test_input, day_3_expected_symbols_collection, day_3_expected_parts_collection
):
    test_parts_collection = identify_part_numbers(
        day_3_test_input, day_3_expected_symbols_collection
    )
    test_part_numbers = [part.part_number for part in test_parts_collection]
    day_3_expected_part_numbers = [
        part.part_number for part in day_3_expected_parts_collection
    ]
    assert test_part_numbers == day_3_expected_part_numbers


def test_calculate_sum_of_part_numbers(
    day_3_test_input, day_3_expected_symbols_collection
):
    test_parts_list = identify_part_numbers(
        day_3_test_input, day_3_expected_symbols_collection
    )
    assert calculate_sum_of_part_numbers(test_parts_list) == 4361


def test_solve_day_3(day_3_test_input):
    assert solve_day_3(day_3_test_input) == (4361, 467835)


@pytest.fixture
def day_3_test_input_custom():
    return [
        "1.*........",
        "..*........",
        "*..........",
    ]


def test_custom_input(day_3_test_input_custom):
    assert solve_day_3(day_3_test_input_custom) == (0, 0)


@pytest.fixture
def day_3_expected_gears_collection(day_3_expected_symbols_collection):
    return [
        day_3_expected_symbols_collection[0],
        day_3_expected_symbols_collection[5],
    ]


def test_identify_gears(
    day_3_test_input, day_3_expected_symbols_collection, day_3_expected_gears_collection
):
    test_parts_list = identify_part_numbers(
        day_3_test_input, day_3_expected_symbols_collection
    )
    output = identify_gears(test_parts_list, day_3_expected_symbols_collection)
    assert output == day_3_expected_gears_collection
