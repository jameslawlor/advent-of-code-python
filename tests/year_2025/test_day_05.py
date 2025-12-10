import pytest
from advent_of_code.year_2025.day_05 import (
    Day05,
    day_05_parser,
    parse_range,
    check_ingredient_fresh,
    compute_total_fresh_ingredients,
    process_ranges,
)

@pytest.fixture
def day_05_test_input_raw():
    return [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]


@pytest.fixture
def day_05_test_input_parsed():
    return [(3,5), (10,14), (16,20), (12,18)], [1, 5, 8, 11, 17, 32]


def test_day_05_parser(day_05_test_input_raw, day_05_test_input_parsed):
    parsed = day_05_parser(day_05_test_input_raw)
    assert parsed == day_05_test_input_parsed


def test_parse_range():
    assert parse_range("3-5") == (3, 5)
    assert parse_range("10-14") == (10, 14)


@pytest.fixture
def day_05_expected_output():
    return (3, 14)


def test_solver(day_05_test_input_raw, day_05_expected_output):
    # Use the Day05 class' solve method (matches the new Problem base API)
    result = Day05().solve(day_05_test_input_raw)
    assert result == day_05_expected_output

@pytest.mark.parametrize(
    "ingredient, fresh_ranges, expected_output",
    [
        (5, [(3,5), (10,14)], True),
        (8, [(3,5), (10,14)], False),
    ],
)   
def test_check_ingredient_fresh(ingredient, fresh_ranges, expected_output):
    assert check_ingredient_fresh(ingredient, fresh_ranges) == expected_output

@pytest.mark.parametrize(
    "fresh_ranges, expected_output",
    [
        ([(3,5), (4,6), (1,7)], 7),
        ([(3,5), (4,6), (8,11)], 8),
        ([(1,1), (2,4), (5,5), (4,4), (7,8)], 7),
        ([(1,2), (1,4), (5,5), (4,5), (7,8)], 7),
    ],
)   
def test_compute_total_fresh_ingredients(fresh_ranges, expected_output):
    assert compute_total_fresh_ingredients(fresh_ranges) == expected_output


@pytest.mark.parametrize(
    "fresh_ranges, expected_output",
    [
        ([(3,5), (4,6), (1,7)], [(1,7)]),
        ([(3,5), (4,6), (9,10)], [(3,6), (9,10)]),
        ([(1,20), (5,9), (15,30)], [(1,30)]),
        ([(3,5), (10,14), (16,20), (12,18)], [(3,5), (10,20)]),
    ],
)   
def test_process_ranges(fresh_ranges, expected_output):
    assert process_ranges(fresh_ranges) == expected_output


    