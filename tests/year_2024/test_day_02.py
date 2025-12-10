import pytest
from advent_of_code.year_2024.day_02 import (
    parse_input,
    solve,
)


@pytest.fixture
def day_02_test_input():
    return [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]


@pytest.fixture
def day_02_expected_output():
    return (2, 4)


def test_solver(day_02_test_input, day_02_expected_output):
    day_02_test_input_parsed = parse_input(day_02_test_input)
    result = solve(day_02_test_input_parsed)
    assert result == day_02_expected_output
