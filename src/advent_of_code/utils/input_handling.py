import argparse


def read_input(f):
    with open(f, "r") as input_file:
        return [line.rstrip("\n") for line in input_file]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
    )
    parser.add_argument("--part", type=int)
    args = parser.parse_args()
    return args


def read_side_by_side_list_format(data):
    list1, list2 = [], []
    for line in data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

    return (list1, list2)
