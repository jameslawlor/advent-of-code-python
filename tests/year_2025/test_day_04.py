import pytest
from advent_of_code.year_2025.day_04 import (
    Day04,
    parse_input_to_array,
    check_is_roll,
    check_roll_accessible,
)
import numpy as np

@pytest.fixture
def day_04_test_input():
    return [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]


@pytest.fixture
def day_04_expected_output():
    return (13, 43)


def test_solver(day_04_test_input, day_04_expected_output):
    # Use the Day04 class' solve method (matches the new Problem base API)
    result = Day04().solve(day_04_test_input)
    assert result == day_04_expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        (
            [
                "..@@",
                "@@@.",
                "@@@@",
            ], 
            np.array(
                [
                    [".",".","@","@"],
                    ["@","@","@","."],
                    ["@","@","@","@"],
                ]
            ),
        ),
    ],
)
def test_parse_input_to_array(input_str, expected_output):
    assert np.array_equal(expected_output, parse_input_to_array(input_str))



@pytest.mark.parametrize(
    "inp_arr, i, j, expected_output",
    [
        (
            np.array(
                [
                    [".",".",],
                    ["@","@",],
                    ["@",".",],
                ]
            ),
            0, 0, False
        ),
        (
            np.array(
                [
                    [".",".",],
                    ["@","@",],
                    ["@",".",],
                ]
            ),
            1, 1, True
        ),
    ],
)
def test_check_is_roll(inp_arr, i, j, expected_output):
    assert expected_output == check_is_roll(inp_arr, i, j)


@pytest.mark.parametrize(
    "i, j, expected",
    [
        (0, 2, True),  
        (1, 1, False),
        (1, 0, True),
        (0, 7, False),
        (0, 8, True),
        (2, 1, False),
    ],
)
def test_check_roll_accessible(day_04_test_input, i, j, expected):
    """Parametrized tests for check_roll_accessible using the provided fixture.

    Each tuple is (i, j, expected) where expected is True if the roll at (i,j)
    has at least one adjacent non-roll cell, and False otherwise.
    
    Fixture with accessible rolls replaced with `x`
        ..xx.xx@x.
        x@@.@.@.@@
        @@@@@.x.@@
        @.@@@@..@.
        x@.@@@@.@x
        .@@@@@@@.@
        .@.@.@.@@@
        x.@@@.@@@@
        .@@@@@@@@.
        x.x.@@@.x.

    """
    arr = parse_input_to_array(day_04_test_input)
    max_i, max_j = arr.shape

    assert check_roll_accessible(arr, i, j, max_i, max_j) is expected
