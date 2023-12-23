all: test solutions

test:
	python3 -m pytest

solutions:
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --part 1
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --part 2