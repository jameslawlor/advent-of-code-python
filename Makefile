all: test solutions

test:
	python3 -m pytest

solutions:
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --no-accept_written_digits
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --accept_written_digits