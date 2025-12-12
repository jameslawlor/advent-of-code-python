import pytest
from advent_of_code.year_2025.day_07 import (
    Day07,
    find_char_on_line,
    update_row,
    process,
    count_splits,
)
import numpy as np

@pytest.fixture
def day_07_test_input_raw():
    return [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]


@pytest.fixture
def day_07_processed_diagram_large():
    return [
        ".......S.......",
        ".......|.......",
        "......|^|......",
        "......|.|......",
        ".....|^|^|.....",
        ".....|.|.|.....",
        "....|^|^|^|....",
        "....|.|.|.|....",
        "...|^|^|||^|...",
        "...|.|.|||.|...",
        "..|^|^|||^|^|..",
        "..|.|.|||.|.|..",
        ".|^|||^||.||^|.",
        ".|.|||.||.||.|.",
        "|^|^|^|^|^|||^|",
        "|.|.|.|.|.|||.|",
    ]

@pytest.fixture
def day_07_test_input_raw_small():
    return [
        [".",".",".","S",".",".",".",],
        [".",".",".",".",".",".",".",],
        [".",".",".","^",".",".",".",],
        [".",".",".",".",".",".",".",],
        [".",".","^",".","^",".",".",],
    ]


@pytest.fixture
def day_07_processed_diagram_small():
    return [
        [".",".",".","S",".",".",".",],
        [".",".",".","|",".",".",".",],
        [".",".","|","^","|",".",".",],
        [".",".","|",".","|",".",".",],
        [".","|","^","|","^","|",".",],
    ]

@pytest.fixture
def day_07_expected_output():
    return (21, None)


def test_solver(day_07_test_input_raw, day_07_expected_output):
    result = Day07().solve(day_07_test_input_raw)
    assert result == day_07_expected_output


@pytest.mark.parametrize(
    "input, char_to_find, expected",
    [
        (['a','b','^','c', 'd', '^'], '^', [2,5,],),
    ],
)   
def test_find_char_on_line(input, char_to_find, expected):
    assert expected == find_char_on_line(input, char_to_find)



@pytest.mark.parametrize(
    "input, loc, expected",
    [
        (
            [".",".",".","^",".",".","."],
            1, 
            [".","|",".","^",".",".","."],
        ),
        (
            [".",".",".","^",".",".","."],
            3, 
            [".",".","|","^","|",".","."],
        ),
    ],
)   
def test_update_row(input, loc, expected):
    assert expected == update_row(input, loc)


def test_process(day_07_test_input_raw_small, day_07_processed_diagram_small):
    assert day_07_processed_diagram_small == process(day_07_test_input_raw_small)


def test_count_splits(day_07_processed_diagram_large):
    assert 21 == count_splits(day_07_processed_diagram_large)