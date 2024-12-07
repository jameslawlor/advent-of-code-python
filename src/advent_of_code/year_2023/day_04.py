from advent_of_code.utils.input_handling import read_input, parse_args

import re


class Card:
    def __init__(self, card_number, winning_numbers, numbers_i_have):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers_i_have = numbers_i_have
        self.n_matches = None
        self.points = None
        self.n_copies = 1

    def __str__(self):
        return (
            f"Card {self.card_number}: {self.winning_numbers} | "
            f"{self.numbers_i_have} | "
            f"n_matches: {self.n_matches} | "
            f"points: {self.points} | "
            f"n_copies: {self.n_copies}"
        )

    def find_n_matches(self):
        self.n_matches = sum(
            [1 for n in self.numbers_i_have if n in self.winning_numbers]
        )

    def compute_points(self):
        if self.n_matches > 0:
            self.points = 2 ** (self.n_matches - 1)
        else:
            self.points = 0


def parse_input_line(line):
    card_number = re.findall(r"(\d+)", line.split(":")[0])[0]
    all_numbers = line.split(":")[1]
    [winning_numbers, numbers_i_have] = all_numbers.split("|")
    winning_numbers = re.findall(r"(\d+)", winning_numbers)
    numbers_i_have = re.findall(r"(\d+)", numbers_i_have)

    return (card_number, winning_numbers, numbers_i_have)


def create_cards(input_txt):
    cards = []
    for line in input_txt:
        (card_number, winning_numbers, numbers_i_have) = parse_input_line(line)
        card = Card(card_number, winning_numbers, numbers_i_have)
        cards.append(card)
    return cards


def compute_total_score(cards):
    total_score = 0
    for card in cards:
        card.find_n_matches()
        card.compute_points()
        total_score += card.points
    return total_score


def compute_copies(cards):
    for card_number, card in enumerate(cards):
        n_matches_on_card = card.n_matches
        n_copies_of_card = card.n_copies
        copies_to_generate = n_copies_of_card
        for next_card in cards[card_number + 1 : card_number + n_matches_on_card + 1]:
            next_card.n_copies += copies_to_generate
    return cards


def solve_day_4(input) -> int:
    cards = create_cards(input)
    total_score = compute_total_score(cards)
    cards_with_copies = compute_copies(cards)
    n_scratchcards = sum([card.n_copies for card in cards_with_copies])
    return (total_score, n_scratchcards)


def main():
    args = parse_args()
    input = read_input(args.input_file)
    result_part_1, result_part_2 = solve_day_4(input)
    print(
        f"Day 4: "
        f" Total points for part 1 is {result_part_1}. "
        f" Total points for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
