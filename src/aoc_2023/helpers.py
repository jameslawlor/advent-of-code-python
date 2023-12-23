import re


def strip_alphabetical_chars_from_string(input_string):
    return re.sub("[^0-9]", "", input_string)


def get_first_last_digits_from_string(input_string):
    input_string_stripped = strip_alphabetical_chars_from_string(input_string)
    first_digit = input_string_stripped[0]
    last_digit = input_string_stripped[-1]
    return first_digit + last_digit


def convert_str_to_numerical(input_string):
    return int(input_string)


def read_input(f):
    with open(f, "r") as input_file:
        return [line.rstrip("\n") for line in input_file]
    

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",)
    parser.add_argument("--input_file",)
    args = parser.parse_args()
    return args


SPELLED_NUMBERS_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def convert_spelled_numbers_to_numerical(input_string):

    spelled_numbers_list = list(SPELLED_NUMBERS_MAPPING.keys())

    numerics_as_strings = [str(x) for x in range (1,10)] 

    patterns_to_find = spelled_numbers_list + numerics_as_strings
    patterns_and_indices = {p:[] for p in patterns_to_find}

    for pattern in patterns_to_find:
        matches = re.finditer(pattern, input_string)
        patterns_and_indices[pattern] = [m.start() for m in matches]

    # find highest and lowest indices
    lowest_index = None
    highest_index = None
    char_at_lowest = ""
    char_at_highest = ""
    for pattern, indices in patterns_and_indices.items():
        if indices:
            tmp_lowest_index = min(indices)
            tmp_highest_index = max(indices)
            
            if lowest_index is None or tmp_lowest_index < lowest_index:
                lowest_index = tmp_lowest_index
                char_at_lowest = pattern
            
            if highest_index is None or tmp_highest_index > highest_index:
                highest_index = tmp_highest_index
                char_at_highest = pattern

    if char_at_lowest in SPELLED_NUMBERS_MAPPING.keys():
        char_at_lowest_as_int = SPELLED_NUMBERS_MAPPING[char_at_lowest]
    else:
        char_at_lowest_as_int = convert_str_to_numerical(char_at_lowest)

    
    if char_at_highest in SPELLED_NUMBERS_MAPPING.keys():
        char_at_highest_as_int = SPELLED_NUMBERS_MAPPING[char_at_highest]
    else:
        char_at_highest_as_int = convert_str_to_numerical(char_at_highest)

    return int(str(char_at_lowest_as_int)+str(char_at_highest_as_int))