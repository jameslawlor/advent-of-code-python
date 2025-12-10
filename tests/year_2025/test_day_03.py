import pytest
from advent_of_code.year_2025.day_03 import (
    calculate_largest_joltage,
    combine_joltages,
    parse_battery_bank_to_ints_list,
    solve,
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


@pytest.mark.parametrize(
    "input_str, expected_output_part_1, expected_output_part_2",
    [
        ("987654321111111", 98, 987654321111),
        ("811111111111119", 89, 811111111119),
        ("234234234234278", 78, 434234234278),
        ("818181911112111", 92, 888911112111),
    ],
)
def test_calculate_largest_joltage(
    input_str, expected_output_part_1, expected_output_part_2
):
    parsed_inputs = parse_battery_bank_to_ints_list(input_str)
    assert expected_output_part_1 == calculate_largest_joltage(
        parsed_inputs, n_batteries=2
    )
    assert expected_output_part_2 == calculate_largest_joltage(
        parsed_inputs, n_batteries=12
    )


def test_parse_battery_bank_to_ints_list():
    assert parse_battery_bank_to_ints_list("98765") == [9, 8, 7, 6, 5]


def test_combine_joltages():
    assert combine_joltages([9, 8, 7]) == 987


@pytest.mark.parametrize(
    "input_str, n_batteries, expected_output",
    [
        ("987", 2, 98),
        ("6781", 2, 81),
        ("19181", 2, 98),
        ("19182", 3, 982),
        ("191821", 3, 982),
    ],
)
def test_calculate_largest_joltage_extra_cases(input_str, expected_output, n_batteries):
    parsed_inputs = parse_battery_bank_to_ints_list(input_str)
    assert expected_output == calculate_largest_joltage(parsed_inputs, n_batteries)
