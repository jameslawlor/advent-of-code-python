import pytest
from aoc_2023.helpers.day_1_solvers import (
    convert_str_to_numerical,
    get_patterns,
    solve_all_calibration_values,
    solve_single_calibration_value,
    find_indices_of_patterns,
    find_first_and_last_patterns,
    convert_first_last_patterns_to_calibration_value,
)


@pytest.mark.parametrize(
    "test_input,expected", [("12", 12), ("38", 38), ("15", 15), ("77", 77)]
)
def test_convert_str_to_numerical(test_input, expected):
    assert convert_str_to_numerical(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (False, [str(x) for x in range(1, 10)]),
        (
            True,
            [str(x) for x in range(1, 10)]
            + ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        ),
    ],
)
def test_get_patterns(test_input, expected):
    assert get_patterns(test_input) == expected


@pytest.mark.parametrize(
    "test_input,patterns_to_find,expected",
    [
        ("1abc2", ["1"], {"1": [0]}),
        ("pqr3stu8vwx", ["8"], {"8": [7]}),
        ("1abc2", ["abc"], {"abc": [1]}),
        ("treb7uchet", ["1", "7"], {"1": [], "7": [4]}),
        ("777", ["abc", "7"], {"abc": [], "7": [0, 1, 2]}),
    ],
)
def test_find_indices_of_patterns(test_input, patterns_to_find, expected):
    assert find_indices_of_patterns(test_input, patterns_to_find) == expected


@pytest.mark.parametrize(
    "test_input_1,test_input_2,expected",
    [
        ("1", "7", 17),
    ],
)
def test_convert_first_last_patterns_to_calibration_value(
    test_input_1, test_input_2, expected
):
    assert (
        convert_first_last_patterns_to_calibration_value(test_input_1, test_input_2)
        == expected
    )


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"1": [0], "2": []}, ("1", "1")),
    ],
)
def test_find_first_and_last_patterns(test_input, expected):
    assert find_first_and_last_patterns(test_input) == expected


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
def test_solve_single_calibration_value(test_input, expected):
    patterns_to_match = get_patterns(accept_written_digits=True)
    assert solve_single_calibration_value(test_input, patterns_to_match) == expected


@pytest.mark.parametrize(
    "test_input,test_accept_written_digits, expected",
    [
        (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ],
            True,
            281,
        ),
        (
            [
                "1abc2",
                "pqr3stu8vwx",
                "a1b2c3d4e5f",
                "treb7uchet",
            ],
            False,
            142,
        ),
    ],
)
def test_solve_all_calibration_values(test_input, test_accept_written_digits, expected):
    test_patterns_to_find = get_patterns(test_accept_written_digits)
    assert solve_all_calibration_values(test_input, test_patterns_to_find) == expected
