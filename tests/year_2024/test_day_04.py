import pytest
from advent_of_code.year_2024.day_04 import (
    solve,
    check_direction_safety,
)

@pytest.mark.parametrize(
    "test_input, expected_result",
    [
        [
            [-1,-1,1,1],
            False,
        ],
        [
            [0,0,1,1],
            True,
        ],
        [
            [2,0,1,1],
            False,
        ],
    ]
)
def test_check_direction_safety(test_input, expected_result):
    result = check_direction_safety(*test_input)
    assert result == expected_result



@pytest.fixture
def day_04_test_input():
    return [
        "MMMSXXMASM",
        # "MSAMXMSMSA",
        # "AMXSXMAAMM",
        # "MSAMASMSMX",
        # "XMASAMXAMM",
        # "XXAMMXXAMA",
        # "SMSMSASXSS",
        # "SAXAMASAAA",
        # "MAMMMXMMMM",
        # "MXMXAXMASX",
    ]


@pytest.fixture
def day_04_expected_output():
    # return (18, None)
    return (1, None)


def test_solve(day_04_test_input, day_04_expected_output):
    result = solve(day_04_test_input)
    assert result == day_04_expected_output

