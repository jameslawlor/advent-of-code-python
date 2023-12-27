import pytest

from aoc_2023.solvers.day_3_solvers import (
    check_char_is_number,
    check_char_is_symbol,
    identify_part_numbers,
    get_symbol_positions,
    get_window,
    check_window_for_symbol,
    calculate_sum_of_part_numbers,
    solve_day_3,
)


@pytest.fixture
def test_symbols():
    return ["=", "/", "*", "@", "$", "+", "%", "#", "-", "&"]


@pytest.fixture
def test_digits():
    return list(map(str, range(10)))


@pytest.fixture
def test_fullstop():
    return ["."]


def test_check_char_is_number(test_symbols, test_digits, test_fullstop):
    output = [check_char_is_number(c) for c in test_symbols]
    assert output == [False] * len(output)

    output = [check_char_is_number(c) for c in test_digits]
    assert output == [True] * len(output)

    output = [check_char_is_number(c) for c in test_fullstop]
    assert output == [False] * len(output)


def test_check_char_is_symbol(test_symbols, test_digits, test_fullstop):
    output = [check_char_is_symbol(c) for c in test_symbols]
    assert output == [True] * len(output)

    output = [check_char_is_symbol(c) for c in test_digits]
    assert output == [False] * len(output)

    output = [check_char_is_symbol(c) for c in test_fullstop]
    assert output == [False] * len(output)


@pytest.fixture
def day_3_test_input():
    return [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]


@pytest.fixture
def day_3_expected_part_numbers():
    return ["467", "35", "633", "617", "592", "755", "664", "598"]


@pytest.fixture
def day_3_expected_symbol_positions():
    return set(
        [
            (1, 3),
            (3, 6),
            (4, 3),
            (5, 5),
            (8, 3),
            (8, 5),
        ]
    )


def test_identify_part_numbers(
    day_3_test_input, day_3_expected_symbol_positions, day_3_expected_part_numbers
):
    assert (
        identify_part_numbers(day_3_test_input, day_3_expected_symbol_positions)
        == day_3_expected_part_numbers
    )


def test_get_symbol_positions(day_3_test_input, day_3_expected_symbol_positions):
    assert get_symbol_positions(day_3_test_input) == day_3_expected_symbol_positions


@pytest.fixture
def test_window():
    return set(
        [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
    )


def test_get_window(test_window):
    """
    Get window around this dummy input of `1`:
    ...
    .1.
    ...
    """
    test_match_start = 1
    test_match_end = 2
    line_number = 1
    test_get_window_output = get_window(test_match_start, test_match_end, line_number)
    assert test_get_window_output == test_window


@pytest.fixture
def test_symbol_positions():
    return set(
        [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
    )


@pytest.mark.parametrize(
    "test_symbol_positions, expected_result",
    [
        (set([(0, 0)]), True),
        (set([(-10, -10)]), False),
    ],
)
def test_check_window_for_symbol(test_window, test_symbol_positions, expected_result):
    assert (
        check_window_for_symbol(test_window, test_symbol_positions) == expected_result
    )


def test_calculate_sum_of_part_numbers(day_3_expected_part_numbers):
    assert calculate_sum_of_part_numbers(day_3_expected_part_numbers) == 4361


def test_solve_day_3(day_3_test_input):
    assert solve_day_3(day_3_test_input) == 4361


@pytest.fixture
def day_3_test_input_custom():
    return [
        "1.*........",
        "..*........",
        "*..........",
    ]


def test_custom_input(day_3_test_input_custom):
    assert solve_day_3(day_3_test_input_custom) == 0
