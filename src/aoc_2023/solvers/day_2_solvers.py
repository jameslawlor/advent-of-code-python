import re

BAG_CONSTRAINTS = {"red": 12, "green": 13, "blue": 14}


def solve_day_2(
    all_games_input,
) -> int:
    sum_of_possible_game_ids = 0
    sum_game_powers = 0
    for full_game_string in all_games_input:
        (game_id, subgames) = parse_game_string(full_game_string)
        max_red = find_max_shown_for_colour(subgames, "red")
        max_blue = find_max_shown_for_colour(subgames, "blue")
        max_green = find_max_shown_for_colour(subgames, "green")
        is_game_possible = check_game_is_possible(max_red, max_blue, max_green)
        if is_game_possible:
            sum_of_possible_game_ids += game_id

        game_power = calculate_game_power(max_red, max_blue, max_green)
        sum_game_powers += game_power
    return sum_of_possible_game_ids, sum_game_powers


def find_max_shown_for_colour(subgames, colour):
    # regex match all bag contents colours
    colours = re.findall(f"(\\d+) {colour}", ";".join(subgames))
    # check if max number shown in game is greater than number in bag
    max_colour = max([int(x) for x in colours])
    return max_colour


def check_game_is_possible(max_red, max_blue, max_green) -> bool:
    # if any colour is shown more than expected, mark as false, otherwise True
    if (
        max_red > BAG_CONSTRAINTS["red"]
        or max_blue > BAG_CONSTRAINTS["blue"]
        or max_green > BAG_CONSTRAINTS["green"]
    ):
        return False
    else:
        return True


def parse_game_string(full_game_str):
    [game_id_prefix, subgames_string] = full_game_str.split(":")
    game_id = int(re.findall("\\d+", game_id_prefix)[0])
    list_of_games = subgames_string.split(";")
    cleaned_list_of_games = [g.strip() for g in list_of_games]
    return (game_id, cleaned_list_of_games)


def calculate_game_power(max_colour_1, max_colour_2, max_colour_3):
    return max_colour_1 * max_colour_2 * max_colour_3
