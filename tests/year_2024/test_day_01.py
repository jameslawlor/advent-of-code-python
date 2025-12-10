import pytest
from advent_of_code.year_2024.day_01 import (
    solve,
)


@pytest.fixture
def day_01_test_input():
    return [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]


@pytest.fixture
def day_01_expected_output():
    return (11, 31)


def test_solver(day_01_test_input, day_01_expected_output):
    result = solve(day_01_test_input)
    assert result == day_01_expected_output
