import pytest

from advent_of_code.year_2025.day_03 import (
    solve,
    calculate_largest_joltage,
    parse_battery_bank_to_ints_list,
    combine_joltages,
)


@pytest.fixture
def day_03_test_input():
    return [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]


@pytest.fixture
def day_03_expected_output():
    return (357, 3121910778619)


def test_solver(day_03_test_input, day_03_expected_output):
    result = solve(day_03_test_input)
    assert result == day_03_expected_output


@pytest.fixture
def test_calculate_largest_joltage_params():
    return [
        ("987654321111111", 98, 987654321111),
        ("811111111111119", 89, 811111111119),
        ("234234234234278", 78, 434234234278),
        ("818181911112111", 92, 888911112111),
    ]

def test_calculate_largest_joltage(test_calculate_largest_joltage_params):
    for input_str, expected_output_part_1, expected_output_part_2 in test_calculate_largest_joltage_params:
        parsed_inputs = parse_battery_bank_to_ints_list(input_str)
        assert expected_output_part_1 == calculate_largest_joltage(parsed_inputs, n_batteries=2)
        assert expected_output_part_2 == calculate_largest_joltage(parsed_inputs, n_batteries=12)

def test_parse_battery_bank_to_ints_list():
    assert parse_battery_bank_to_ints_list("98765") == [9,8,7,6,5]

def test_combine_joltages():
    assert combine_joltages([9, 8, 7]) == 987