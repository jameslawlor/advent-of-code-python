import pytest
from advent_of_code.year_2023.solvers.day_2_solvers import (
    solve_day_2,
    check_game_is_possible,
    parse_game_string,
    find_max_shown_for_colour,
)


@pytest.fixture
def day_2_test_input():
    return [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]


@pytest.mark.parametrize("expected", [(8, 2286)])
def test_solve_day_2(day_2_test_input, expected):
    assert solve_day_2(day_2_test_input) == expected


@pytest.mark.parametrize("expected", [(True, True, False, False, True)])
def test_check_game_is_possible(day_2_test_input, expected):
    for game, expected_result in zip(day_2_test_input, expected):
        _, test_game = parse_game_string(game)
        max_red = find_max_shown_for_colour(test_game, "red")
        max_blue = find_max_shown_for_colour(test_game, "blue")
        max_green = find_max_shown_for_colour(test_game, "green")
        assert check_game_is_possible(max_red, max_blue, max_green) == expected_result


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["1 red; 12 red"], 12),
    ],
)
def test_find_max_shown_for_colour(test_input, expected):
    find_max_shown_for_colour(test_input, "red") == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue",
            (1, ["3 blue, 4 red", "1 red, 2 green, 6 blue"]),
        )
    ],
)
def test_parse_game_string(test_input, expected):
    assert parse_game_string(test_input) == expected
