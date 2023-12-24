import argparse


def read_input(f):
    with open(f, "r") as input_file:
        return [line.rstrip("\n") for line in input_file]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part",
    )
    parser.add_argument(
        "--input_file",
    )
    parser.add_argument(
        "--accept_written_digits",
    )
    args = parser.parse_args()
    return args
