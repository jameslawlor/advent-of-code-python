import pytest

from aoc_2023.helpers.day_3_solvers import (
    find_schematic_size,
    convert_raw_schematic_to_array,
    find_symbol_indices,
    find_adjacent_numbers,
    identify_part_numbers,
)

@pytest.fixture
def day_3_test_input():
    raw_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    return raw_text.split("\n")


def test_day_3_test_input(day_3_test_input):
    print()
    print(day_3_test_input)


@pytest.mark.parametrize(
    "expected",
    [
        (10,10)
    ],
)
def test_find_schematic_size(day_3_test_input, expected):
    assert find_schematic_size(day_3_test_input) == expected


# def test_convert_raw_schematic_to_array(day_3_test_input, expected):
#     assert convert_raw_schematic_to_array(day_3_test_input) == expected

@pytest.mark.parametrize(
    "expected",
    [
        (1,3),
        (3,6),
        (4,3),
        (5,5),
        (8,3),
        (8,5),
    ],
)
def test_find_symbol_indices(day_3_test_input, expected):
    assert find_symbol_indices(day_3_test_input) == expected


@pytest.mark.parametrize(
    "expected",
    [
        
    ],
)
def test_find_adjacent_numbers(day_3_test_input, expected):
    assert find_adjacent_numbers(day_3_test_input) == expected


@pytest.mark.parametrize(
    "expected",
    [
        (1,3),
        (3,6),
        (4,3),
        (5,5),
        (8,3),
        (8,5),
    ],
)
def test_identify_part_numbers(day_3_test_input, expected):
    assert identify_part_numbers(day_3_test_input) == expected

