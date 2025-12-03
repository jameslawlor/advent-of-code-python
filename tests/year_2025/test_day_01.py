import pytest
from advent_of_code.year_2025.day_01 import (
    solve,
    turn_dial,
    position_counter,
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

@pytest.fixture(params=[
        (50 ,    -1    , 68 , 82    , 0 , 1 ),
        (82 ,    -1    , 30 , 52    , 0 , 0 ),
        (52 ,    1     , 48 , 0     , 1 , 1 ), 
        (0  ,    -1    , 5  , 95    , 0 , 0 ),
        (95 ,    1     , 60 , 55    , 0 , 1 ),
        (55 ,    -1    , 55 , 0     , 1 , 1 ),
        (0  ,    -1    , 1  , 99    , 0 , 0 ),
        (99 ,    -1    , 99 , 0     , 1 , 1 ),
        (0  ,    1     , 14 , 14    , 0 , 0 ),
        (14 ,    -1    , 82 , 32    , 0 , 1 ),
    ],
)
def turn_case(request):
    """
    (current_position, turn_direction, distance, expected_new_position, part_1_count, part_2_count)

    """
    return request.param

def test_turn_dial(turn_case):
    current_position, turn_direction, distance, expected_new_position, _, _ = turn_case
    new_position = turn_dial(current_position, turn_direction, distance)
    assert new_position == expected_new_position


def test_position_counter(turn_case):
    _, _, _, expected_new_position, expected_count, _ = turn_case
    actual_count = position_counter(expected_new_position)
    assert actual_count == expected_count


# @pytest.mark.parametrize(
#     "start_position, turn_direction, distance, expected_count",
#     [
#         (50, 1, 1000, 10),
#         # (50, 1, 49, 0),
#         # (50, -1, 49, 0),
#         # (50, -1, 50, 1),
#         # (50, -1, 51, 1),
#         # (99, 1, 1, 1),
#         # (99, -1, 1, 0),
#         # (0, 1, 100, 1),
#     ]
# )
# def test_passing_zero_counter(start_position, turn_direction, distance, expected_count):
#     count = passing_zero_counter(start_position, turn_direction, distance)
#     assert count == expected_count