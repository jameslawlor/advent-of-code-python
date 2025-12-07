import pytest

from advent_of_code.year_2023.day_04 import (
    compute_copies,
    compute_total_score,
    create_cards,
    solve_day_4,
)


@pytest.fixture
def day_4_test_input():
    return [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]


@pytest.fixture
def day_4_expected_scores():
    return [
        8,
        2,
        2,
        1,
        0,
        0,
    ]


@pytest.fixture
def day_4_expected_final_cards_count():
    return [1, 2, 4, 8, 14, 1]


def test_day_4_expected_final_cards_count(day_4_expected_final_cards_count):
    assert sum(day_4_expected_final_cards_count) == 30


def test_solve_day_4(
    day_4_test_input, day_4_expected_scores, day_4_expected_final_cards_count
):
    assert solve_day_4(day_4_test_input) == (
        sum(day_4_expected_scores),
        sum(day_4_expected_final_cards_count),
    )


def test_compute_copies(day_4_test_input, day_4_expected_final_cards_count):
    test_cards = create_cards(day_4_test_input)
    compute_total_score(test_cards)
    test_cards_with_copies = compute_copies(test_cards)
    test_n_scratchcards = [card.n_copies for card in test_cards_with_copies]
    assert test_n_scratchcards == day_4_expected_final_cards_count
