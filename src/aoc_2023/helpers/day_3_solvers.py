import numpy as np

def find_schematic_size(input):
    size_y = len(input)
    size_x = len(input[0])
    for line in input[1:]:
        if len(line) != size_x:
            raise ValueError("Invalid array size! Check input format...")
    return (size_x, size_y)


def convert_raw_schematic_to_array(input):
    return np.array(input)


def find_symbol_indices():
    return 


def find_adjacent_numbers():
    return 


def identify_part_numbers():
    return 

