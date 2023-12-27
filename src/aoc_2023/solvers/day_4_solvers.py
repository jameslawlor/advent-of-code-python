import re


class Card:
    def __init__(self, card_number, winning_numbers, numbers_i_have):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers_i_have = numbers_i_have
        self.n_winners = None
        self.points = None

    def __str__(self):
        return (
            f"Card {self.card_number}: {self.winning_numbers} | "
            f"{self.numbers_i_have} | "
            f"n_winners: {self.n_winners} | points: {self.points}"
        )

    def find_n_winners(self):
        self.n_winners = sum(
            [1 for n in self.numbers_i_have if n in self.winning_numbers]
        )

    def compute_points(self):
        if self.n_winners > 0:
            self.points = 2 ** (self.n_winners - 1)
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
        card.find_n_winners()
        card.compute_points()
        total_score += card.points
    return total_score


def solve_day_4(input) -> int:
    cards = create_cards(input)
    total_score = compute_total_score(cards)
    return total_score
