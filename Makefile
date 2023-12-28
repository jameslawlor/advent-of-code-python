all: black flake test solutions 

black:
	black ./src ./tests

flake:
	flake8 ./src ./tests

test:
	python3 -m pytest

solutions:
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --part 1
	python3 src/aoc_2023/days/1.py --input_file inputs/1.txt --part 2
	python3 src/aoc_2023/days/2.py --input_file inputs/2.txt
	python3 src/aoc_2023/days/3.py --input_file inputs/3.txt
	python3 src/aoc_2023/days/4.py --input_file inputs/4.txt
	python3 src/aoc_2023/days/6.py --input_file inputs/6.txt