from advent_of_code.utils.input_handling import read_input

def is_report_safe(report,):
    if not ((report==sorted(report)) or (report==sorted(report,reverse=True))):
        return False

    differences = [abs(report[i+1] - report[i]) for i in range(len(report) - 1)]
    if ((max(differences) > 3) or (min(differences)<1)):
        return False

    return True


def solve_part_1(input):
    safe_report_count = 0
    for report in input:
        if is_report_safe(report):
            safe_report_count += 1
    return safe_report_count


def solve_part_2(input,):

    safe_report_count = 0

    for report in input:
        if is_report_safe(report):
            safe_report_count += 1
        else:
            for idx, _ in enumerate(report):
                tmp_report = report[:]
                del tmp_report[idx]
                if is_report_safe(tmp_report,):
                    safe_report_count += 1
                    break
    return safe_report_count


def solve(input):
    part_1_solution = solve_part_1(input)
    part_2_solution = solve_part_2(input)
    return (part_1_solution, part_2_solution)


def parse_input(input_data,dtype=int):
    data = [list(map(dtype, line.rstrip("\n").split())) for line in input_data]
    return data


def main(input_file):
    unparsed_input = read_input(input_file)
    parsed_input = parse_input(unparsed_input)
    (result_part_1, result_part_2) = solve(parsed_input)
    print(
        f"Day 02: "
        f" Result for part 1 is {result_part_1}. "
        f" Result for part 2 is {result_part_2}. "
    )


if __name__ == "__main__":
    main()
