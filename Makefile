.PHONY: all clean black flake test solutions 

# Default target
all: ruff test solutions clean

# Clean temporary and generated files
clean:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf

# Format code using black
ruff:
	ruff check .

# Run tests
test:
	python3 -m pytest

# Run specific solutions for Advent of Code 2023
solutions:
	python3 src/advent_of_code/year_2023/days/1.py --input_file inputs/2023/01.txt --part 1
	python3 src/advent_of_code/year_2023/days/1.py --input_file inputs/2023/01.txt --part 2
	python3 src/advent_of_code/year_2023/days/2.py --input_file inputs/2023/02.txt
	python3 src/advent_of_code/year_2023/days/3.py --input_file inputs/2023/03.txt
	python3 src/advent_of_code/year_2023/days/4.py --input_file inputs/2023/04.txt
	python3 src/advent_of_code/year_2023/days/6.py --input_file inputs/2023/06.txt

.PHONY: new-day-skeleton-files-from-template
new-day-skeleton-files-from-template:
	@read -p "Enter year: " year; \
	read -p "Enter day: " day; \
	python3 src/advent_of_code/scripts/generate_new_day_skeleton_files_from_templates.py --day $$day --year $$year