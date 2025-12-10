from advent_of_code.utils.problem import Problem
import numpy as np

def parse_input_to_array(inp):
    tmp = []
    for line in inp:
        tmp.append([x for x in line])
    return np.array(tmp)

def check_is_roll(arr, i, j, roll_char="@"):
    if arr[i, j] == roll_char:
        return True
    else:
        return False

def check_roll_accessible(arr, i, j, max_i, max_j):

    threshold = 4
    neighbouring_roll_count = 0

    # check above
    if i > 0:
        if check_is_roll(arr, i-1, j):
            neighbouring_roll_count += 1
        
    # check above and right
    if i > 0 and j < max_j - 1:
        if check_is_roll(arr, i-1, j+1):
            neighbouring_roll_count += 1
        
    # check above and left
    if i > 0 and j > 0:
        if check_is_roll(arr, i-1, j-1):
            neighbouring_roll_count += 1
        
    # check right
    if j < max_j - 1:
        if check_is_roll(arr, i, j+1):
            neighbouring_roll_count += 1
        
    # check below and right
    if i < max_i - 1 and j < max_j - 1:
        if check_is_roll(arr, i+1, j+1):
            neighbouring_roll_count += 1
        
    # check below
    if i < max_i - 1:
        if check_is_roll(arr, i+1, j):
            neighbouring_roll_count += 1
        
    # check below and left
    if i < max_i - 1 and j > 0:
        if check_is_roll(arr, i+1, j-1):
            neighbouring_roll_count += 1
    
    # check left
    if j > 0:
        if check_is_roll(arr, i, j-1):
            neighbouring_roll_count += 1
    
    if neighbouring_roll_count >= threshold:
        return False
    else:
        return True


def check_whole_array(arr):
    max_i, max_j = arr.shape
    accessible_rolls_indices = []
    for i in range(max_i):
        for j in range(max_j):
            if check_is_roll(arr, i, j):
                if check_roll_accessible(arr, i, j, max_i, max_j):
                    accessible_rolls_indices.append((i, j))
    return accessible_rolls_indices


def update_array(arr, indices_to_remove, replacement_char="."):
    for (i, j) in indices_to_remove:
        arr[i, j] = replacement_char
    return arr

class Day04(Problem):
    YEAR = 2025
    DAY = 4

    def part1(self, input_lines):
        arr = parse_input_to_array(input_lines)
        result = len(check_whole_array(arr))
        return result

    def part2(self, input_lines):
        arr = parse_input_to_array(input_lines)
        total_rolls_removed = 0
        rolls_removed_this_iteration = 1

        while rolls_removed_this_iteration > 0:
            result = check_whole_array(arr)
            rolls_removed_this_iteration = len(result)
            total_rolls_removed += rolls_removed_this_iteration
            arr = update_array(arr, result)
        return total_rolls_removed

main = Day04.main

if __name__ == "__main__":
    Day04.main()
