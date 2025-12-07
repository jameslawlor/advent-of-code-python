import pytest

from advent_of_code.year_2025.day_01 import (
    points_at_zero_counter,
    solve,
    target_position_counter,
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
    return (3, 6)


def test_solver(day_01_test_input, day_01_expected_output):
    result = solve(day_01_test_input)
    assert result == day_01_expected_output


@pytest.fixture(
    params=[
        (50, -1, 68, 82, 0, 1),  # case 0
        (82, -1, 30, 52, 0, 0),  # case 1
        (52, 1, 48, 0, 1, 1),  # case 2
        (0, -1, 5, 95, 0, 0),  # case 3
        (95, 1, 60, 55, 0, 1),  # case 4
        (55, -1, 55, 0, 1, 1),  # case 5
        (0, -1, 1, 99, 0, 0),  # case 6
        (99, -1, 99, 0, 1, 1),  # case 7
        (0, 1, 14, 14, 0, 0),  # case 8
        (14, -1, 82, 32, 0, 1),  # case 9
    ],
)
def turn_case(request):
    """
    (current_position, turn_direction, distance,
     expected_new_position, part_1_count, part_2_count)

    """
    return request.param


def test_turn_dial(turn_case):
    current_position, turn_direction, distance, expected_new_position, _, _ = turn_case
    new_position = turn_dial(current_position, turn_direction, distance)
    assert new_position == expected_new_position


def test_target_position_counter(turn_case):
    _, _, _, expected_new_position, expected_count, _ = turn_case
    actual_count = target_position_counter(expected_new_position)
    assert actual_count == expected_count


def test_points_at_zero_counter(turn_case):
    current_position, turn_direction, distance, _, _, expected_count = turn_case
    actual_count = points_at_zero_counter(current_position, turn_direction, distance)
    assert actual_count == expected_count


@pytest.mark.parametrize(
    "start_position, turn_direction, distance, expected_count",
    [
        (50, 1, 1000, 10),
        (50, 1, 1050, 11),
        (0, 1, 100, 1),
        (0, 1, 200, 2),
        (0, 1, 1, 0),
        (50, -1, 68, 1),
        (50, 1, 68, 1),
    ],
)
def test_points_at_zero_counter_extra_test_cases(
    start_position, turn_direction, distance, expected_count
):
    count = points_at_zero_counter(start_position, turn_direction, distance)
    assert count == expected_count
