from advent_of_code.utils.problem import Problem

START_CHAR = "S"
EMPTY_CHAR = "."
BEAM_CHAR = "|"
SPLITTER_CHAR = "^"

def parse_input(input_rows):
    return [[_ for _ in l] for l in input_rows]


def find_char_on_line(line, char_to_find):
    matched_indices = []
    for index, c in enumerate(line):
        if c == char_to_find:
            matched_indices.append(index)
    return matched_indices


def update_row(row, loc):
    # row_as_list = [c for c in row[0]]
    right_index = loc + 1
    left_index = loc - 1
    # if we hit splitter, split the beam
    if row[loc] == SPLITTER_CHAR:
        # check neighbouring cells exist and fill
        if len(row) > right_index:
            row[right_index] = BEAM_CHAR
        if left_index >= 0:
            row[left_index] = BEAM_CHAR
            
    # if loc empty, beam continues 
    elif row[loc] == EMPTY_CHAR:
        row[loc] = BEAM_CHAR
    
    return row

def process(input_diagram):
    first_row = input_diagram[0]
    incoming_beam_locations = find_char_on_line(
        first_row,
        START_CHAR,
    )
    output_diagram = [first_row]
    print(f"incoming_beam_locations={incoming_beam_locations}")
    for row in input_diagram[1:]:
        # Update indices where there's an incoming beam
        print(f"updating with {incoming_beam_locations}")
        print(f"row before = {row}")
        for loc in incoming_beam_locations:
            row = update_row(row, loc)
        print(f"row after = {row}")
        output_diagram.append(row)
        incoming_beam_locations =  find_char_on_line(
            row,
            BEAM_CHAR,
        )
        
    return output_diagram

def count_splits(arr):
    cnt = 0

    # Count each time a splitter is hit by beam from above
    for row_index in range(1, len(arr)):

        row_to_check = arr[row_index]
        splitters_on_row = find_char_on_line(
            row_to_check,
            SPLITTER_CHAR, 
        )

        row_above = arr[row_index - 1]
        incoming_beam_locations =  find_char_on_line(
            row_above,
            BEAM_CHAR,
        )

        for splitter_index in splitters_on_row:
            if splitter_index in incoming_beam_locations:
                cnt+=1
    return cnt

class Day07(Problem):
    YEAR = 2025
    DAY = 7

    def part1(self, input_lines):
        input_diagram = parse_input(input_lines)
        processed_diagram = process(input_diagram)
        n_splits = count_splits(processed_diagram)
        return n_splits

    def part2(self, input_lines):
        input_diagram = parse_input(input_lines)
    
main = Day07.main

if __name__ == "__main__":
    Day07.main()
