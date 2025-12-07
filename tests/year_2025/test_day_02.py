import pytest

from advent_of_code.year_2025.day_02 import (
    check_id_valid,
    convert_range_string_to_pair,
    find_invalid_ids_in_range_string,
    parse_input,
    solve,
    sum_invalid_ids,
)


@pytest.mark.parametrize(
    "input, expected_output",
    [
        [
            [
                "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"  # noqa: E501
            ],
            (1227775554, None),
        ],
    ],
)
def test_solver(input, expected_output):
    print(f"day_02_test_input:{input}")
    input_parsed = parse_input(input)
    print(f"input_parsed:{input_parsed}")
    result = solve(input_parsed)
    assert result == expected_output


@pytest.mark.parametrize(
    "input, expected_invalid_ids",
    [
        ["11-22", [11, 22]],
        ["95-115", [99]],
        ["998-1012", [1010]],
        ["1188511880-1188511890", [1188511885]],
        ["222220-222224", [222222]],
        ["1698522-1698528", []],
        ["446443-446449", [446446]],
        ["38593856-38593862", [38593859]],
        ["565653-565659", []],
        ["824824821-824824827", []],
        ["2121212118-2121212124", []],
    ],
)
def test_find_invalid_ids_in_range_string(input, expected_invalid_ids):
    assert expected_invalid_ids == find_invalid_ids_in_range_string(input)


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ([1, 2, 3], 6),
    ],
)
def test_sum_invalid_ids(input, expected_output):
    assert expected_output == sum_invalid_ids(input)


@pytest.mark.parametrize(
    "input, expected_pair",
    [
        ("11-22", (11, 22)),
        ("95-115", (95, 115)),
        ("998-1012", (998, 1012)),
        ("1188511880-1188511890", (1188511880, 1188511890)),
    ],
)
def test_convert_range_string_to_pair(input, expected_pair):
    assert expected_pair == convert_range_string_to_pair(input)


@pytest.mark.parametrize(
    "input, is_valid",
    [("11", False), ("12", True), ("22", False), ("998", True), ("1010", False)],
)
def test_check_id_valid(input, is_valid):
    assert is_valid == check_id_valid(input)
