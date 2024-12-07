from advent_of_code.utils.input_handling import read_input, read_side_by_side_list_format

def compute_distance(i, j):
    return abs(i - j)


def solve_part_1(parsed_input):
    (list1, list2) = parsed_input
    list1_ordered = list(sorted(list1))
    list2_ordered = list(sorted(list2))

    total_distance = 0

    for i, j in zip(list1_ordered, list2_ordered):
        total_distance += compute_distance(i, j)

    return total_distance


def compute_similarity(i, lst):
    return i * lst.count(i)


def solve_part_2(parsed_input):
    (list1, list2) = parsed_input

    total_similarity_score = 0

    for element in list1:
        total_similarity_score += compute_similarity(element, list2)

    return total_similarity_score



def solve(input):
    parsed_input = read_side_by_side_list_format(input)
    part_1_solution = solve_part_1(parsed_input)
    part_2_solution = solve_part_2(parsed_input)
    return (part_1_solution, part_2_solution)


def main(input_file):
    input = read_input(input_file)
    (result_part_1, result_part_2) = solve(input)
    print(
        f"Day 01: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
