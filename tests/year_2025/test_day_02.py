import pytest

from advent_of_code.year_2025.day_02 import (
    check_id_valid,
    check_id_valid_v2,
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
            (1227775554, 4174379265),
        ],
    ],
)
def test_solver(input, expected_output):
    print(f"day_02_test_input:{input}")
    input_parsed = parse_input(input)
    print(f"input_parsed:{input_parsed}")
    result = solve(input_parsed)
    assert result == expected_output

# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.

@pytest.mark.parametrize(
    "input, expected_invalid_ids",
    [
        ["11-22", [11, 22]],
        ["95-115", [99, 111]],
        ["998-1012", [999, 1010]],
        ["1188511880-1188511890", [1188511885]],
        ["222220-222224", [222222]],
        ["1698522-1698528", []],
        ["446443-446449", [446446]],
        ["38593856-38593862", [38593859]],
        ["565653-565659", [565656]],
        ["824824821-824824827", [824824824]],
        ["2121212118-2121212124", [2121212121]],
    ],
)
def test_find_invalid_ids_in_range_string_part_2(input, expected_invalid_ids):
    assert expected_invalid_ids == find_invalid_ids_in_range_string(input, part=2)

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
    assert expected_invalid_ids == find_invalid_ids_in_range_string(input, part=1)


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
    [("11", False), ("12", True), ("22", False), ("998", True), ("999", True), ("1010", False), ("565656", True)],
)
def test_check_id_valid(input, is_valid):
    assert is_valid == check_id_valid(input)

@pytest.mark.parametrize(
    "input, is_valid",
    [
        ("11", False), 
        ("12", True), 
        ("22", False), 
        ("998", True), 
        ("999", False), 
        ("1010", False),
        ("565656", False),
    ],
)
def test_check_id_valid_v2(input, is_valid):
    assert is_valid == check_id_valid_v2(input)
