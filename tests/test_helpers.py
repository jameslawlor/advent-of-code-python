import pytest
from aoc_2023.helpers import (
    get_first_last_digits_from_string,
    strip_alphabetical_chars_from_string,
    convert_str_to_numerical,
    convert_spelled_numbers_to_numerical,
)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", "12"),
        ("pqr3stu8vwx", "38"),
        ("a1b2c3d4e5f", "12345"),
        ("treb7uchet", "7"),
    ],
)
def test_strip_alphabetical_chars_from_string(test_input, expected):
    assert strip_alphabetical_chars_from_string(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", ("12")),
        ("pqr3stu8vwx", ("38")),
        ("a1b2c3d4e5f", ("15")),
        ("treb7uchet", ("77")),
    ],
)
def test_get_first_last_digits_from_string(test_input, expected):
    assert get_first_last_digits_from_string(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [("12", 12), ("38", 38), ("15", 15), ("77", 77)]
)
def test_convert_str_to_numerical(test_input, expected):
    assert convert_str_to_numerical(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("oneightone", 11),
    ],
)
def test_convert_spelled_numbers_to_numerical(test_input, expected):
    assert convert_spelled_numbers_to_numerical(test_input) == expected
    