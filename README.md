# advent-of-code-python

Some overengineered Python solutions for Advent of Code 2023

Quick docker run (same behavior as running the package locally):

```
docker build -t advent-of-code-python-app .
docker run advent-of-code-python-app
```

Running solutions (recommended)

This project exposes a small CLI entrypoint implemented in `src/advent_of_code/cli.py`.
There are three common ways to run a day's solution:

- Run directly from the repository (no install):

	```
	PYTHONPATH=src python -m advent_of_code --year 2025 --day 1
	```

- Run with the module flag (if you have the package importable):

	```
	python -m advent_of_code --year 2025 --day 1
	```

- Install editable and use the console script (recommended for convenience):

	```
	pip install -e .
	aoc --year 2025 --day 1
	```

Notes on invocation

- The CLI expects `--year` and `--day`. The `--day` value accepts either `1` or `01` — the code zero-pads the value to match input filenames.
- Input files live under `inputs/year_<YYYY>/<NN>.dat` where `<NN>` is zero-padded to two digits (e.g. `01.dat`).
- Each day module under `src/advent_of_code/year_<YYYY>/day_<NN>.py` should expose a `main(input_file)` function which the CLI calls.
- If you see "Could not find module" when running the CLI, either install the package (`pip install -e .`) or run with `PYTHONPATH=src` as shown above.

Dependencies and `uv`

- Project dependencies are listed in `pyproject.toml` and `requirements.txt`.
- This repository includes `uv` (version pinned in `requirements.txt` / `pyproject.toml`) as a dependency. Installing the project (or the requirements) will pull `uv` in. The core day-runner CLI (`aoc` / `python -m advent_of_code`) does not require `uv` to run a solution file, but `uv` is available for any tooling or extensions that may use it.

Installing dependencies

```
pip install -r requirements.txt
# or for editable install (recommended if you want the `aoc` console script):
pip install -e .
```

Scripts

- `scripts/run_day.py` — a small script that mirrors the CLI behavior but can be invoked directly with Python.
- `scripts/run_all_solutions.py` — discovers and runs available day solutions (skips days without an input file).

### 2025 Progress

| Day   | Part 1 | Part 2 |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |
| 04 | ⭐️ | ⭐️ |

### 2024 Progress

| Day   | Part 1 | Part 2 |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |

### 2023 Progress

| Day   | Part 1 | Part 2 |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |
| 04 | ⭐️ | ⭐️ |
| 05 | todo | todo |
| 06 | ⭐️ | ⭐️ |