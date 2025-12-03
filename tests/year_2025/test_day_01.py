import pytest
from advent_of_code.year_2025.day_01 import (
    solve,
    turn_dial,
)


@pytest.fixture
def day_01_test_input():
    return [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]


@pytest.fixture
def day_01_expected_output():
    return (3, None)


def test_solver(day_01_test_input, day_01_expected_output):
    result = solve(day_01_test_input)
    assert result == day_01_expected_output

@pytest.mark.parametrize(
    "current_position, turn_direction, distance, expected_new_position",
    [
        (50, -1, 68, 82),
        (82, -1, 30, 52),
        (52, 1, 48, 0), 
        (0, -1, 5, 95),
        (95, 1, 60, 55),
        (55, -1, 55, 0),
        (0, -1, 1, 99),
        (99, -1, 99, 0),
        (0, 1, 14, 14),
        (14, -1, 82, 32),
    ],
)
def test_turn_dial(current_position, turn_direction, distance, expected_new_position):
    new_position = turn_dial(current_position, turn_direction, distance)
    assert new_position == expected_new_position
