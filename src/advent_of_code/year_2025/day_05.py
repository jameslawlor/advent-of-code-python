from advent_of_code.utils.problem import Problem
from itertools import groupby

def day_05_parser(raw_input):
    delim = ""
    groups = groupby(raw_input, lambda x: x==delim)
    l = [list(group) for is_delim, group in groups if not is_delim]
    fresh_ranges = [parse_range(r) for r in l[0]]
    available_ingredients = [int(i) for i in l[1]]
    return fresh_ranges, available_ingredients
    

def parse_range(range_str):
    start_str, end_str = range_str.split('-')
    return int(start_str), int(end_str)


def check_ingredient_fresh(ingredient, fresh_ranges):
    for r in fresh_ranges:
        if ingredient > r[0] and ingredient <= r[1]+1:
            return True
    return False


def process_ranges(fresh_ranges):
    """
    Convert list of overlapping ranges 
    by combining into non-overlapping ones
    """
    fresh_ranges_sorted = sorted(list(fresh_ranges))
    output = [fresh_ranges_sorted[0]]

    for range_start, range_end in fresh_ranges_sorted[1:]:
        for ix, (output_range_start, output_range_end) in enumerate(output):
            # determine kind of overlap, if any

            # range starts in window, ends outside
            # so extend output_range_end
            if range_start > output_range_start \
                and range_start < output_range_end \
                and range_end > output_range_end:
                output[ix] = (output_range_start, range_end)
                break

            elif range_start < output_range_start \
                and range_end > output_range_start \
                and range_end < output_range_end:
                output[ix] = (range_start, output_range_end)
                break

            # range starts out of window, ends outside
            # so extend both
            elif range_start < output_range_start \
                and range_end > output_range_end:
                
                output[ix] = (range_start, range_end)

                break

            # range fully inside existing output range
            elif range_start >= output_range_start \
                and range_end <= output_range_end:
                break  

            # range start coincides, but range ends outside
            elif range_start == output_range_start \
                and range_end > output_range_end:
                output[ix] = (range_start, range_end)
                break

            # range start coincides with outpout range end
            elif range_start == output_range_end:
                output[ix] = (output_range_start, range_end)
                break

            # range end coincides, but range start outside
            elif range_start < output_range_start \
                and range_end == output_range_end:
                output[ix] = (range_start, range_end)
                break

            # otherwise we have a new range to add
            if ix == len(output) - 1:
                output.append((range_start, range_end))
                break

    return output

def compute_total_fresh_ingredients(fresh_ranges):
    processed_ranges = process_ranges(fresh_ranges)

    total = 0
    for range_start, range_end in processed_ranges:
        total += range_end - range_start + 1
    return total

class Day05(Problem):
    YEAR = 2025
    DAY = 5

    def part1(self, input_lines):
        fresh_ranges, available_ingredients = day_05_parser(input_lines)
        fresh_count = 0
        for ingredient in available_ingredients:
            if check_ingredient_fresh(ingredient, fresh_ranges):
                fresh_count += 1
        return fresh_count

    def part2(self, input_lines):
        fresh_ranges, _ = day_05_parser(input_lines)
        return compute_total_fresh_ingredients(fresh_ranges)

main = Day05.main

if __name__ == "__main__":
    Day05.main()
