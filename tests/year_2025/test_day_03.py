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
    return (357, None)


def test_solver(day_03_test_input, day_03_expected_output):
    result = solve(day_03_test_input)
    assert result == day_03_expected_output

@pytest.mark.parametrize(
    "input, expected_output",
    [
        [[9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],98],
        [[8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],89],
        [[2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],78],
        [[8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],92],
    ],
)
def test_calculate_largest_joltage(input, expected_output):
    parsed_inputs = parse_battery_bank_to_ints_list(input)
    assert expected_output == calculate_largest_joltage(parsed_inputs)


def test_parse_battery_bank_to_ints_list():
    assert parse_battery_bank_to_ints_list("98765") == [9,8,7,6,5]

def test_combine_joltages():
    assert combine_joltages(9, 8) == 98