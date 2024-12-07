
import re
import math

DO_SUBSTR = 'do()'
DONT_SUBSTR = 'don\'t()'

def find_valid_substrings(s, match_str=r'mul\(\d+,\d+\)'):
    return re.findall(match_str, s)

def find_and_multiply_valid_muls_in_string(input_string):
    string_score = 0
    valid_muls = find_valid_substrings(input_string)
    for m in valid_muls:
        found_ints = find_valid_substrings(m, match_str=r'\d+')
        string_score += math.prod(map(int, found_ints))
    return string_score

def instruction_compute(instruction, use_do_dont_rule=False):

    if not use_do_dont_rule:
        instruction_score = find_and_multiply_valid_muls_in_string(instruction)
    else:
        instruction_score=0
        padded_instruction = DO_SUBSTR+instruction.strip("\n")+DONT_SUBSTR
        valid_subs = find_valid_substrings(
            padded_instruction, 
            match_str=r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
            )
        counting_active = False
        for (i, j, do, dont) in valid_subs:
            if do:
                counting_active = True
            elif dont:
                counting_active = False
            else:
                if counting_active:
                    instruction_score += int(i)*int(j)
    return instruction_score

def solve(input):

    part_1_solution, part_2_solution = 0, 0
    part_1_solution = instruction_compute(input, False)
    part_2_solution = instruction_compute(input, True)
    return (part_1_solution, part_2_solution)


def main(input_file):
    input = input = open(input_file).read()
    (result_part_1, result_part_2) = solve(input)
    print(
        f"Day 03: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
