from advent_of_code.utils.input_handling import read_input
import numpy as np

STRING_TO_FIND = 'XMAS'

DIRECTIONS = [
    (0, 1),  
    (0, -1), 
    (1, 0),  
    (-1, 0), 
    (1, 1),  
    (1, -1), 
    (-1, 1), 
    (-1, -1) 
]

def check_direction_safety(i,j,nrows,ncols):
    if (
        (i < 0) or
        (i >= nrows) or
        (j < 0) or
        (j > ncols)
    ):
        return False
    else:
        return True


def solve(input):
    input_parsed = np.array([list(row) for row in input])
    nrows, ncols = input_parsed.shape
    print(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            character = input_parsed[i,j]
            if character == STRING_TO_FIND[0]:
                for direction in DIRECTIONS:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    direction_is_safe = check_direction_safety(new_i,new_j,nrows,ncols)
                    if direction_is_safe
    return (18, None)


def main(input_file):
    input = read_input(input_file)
    (result_part_1, result_part_2) = solve(input)
    print(
        f"Day 04: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
