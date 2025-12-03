<!-- Copilot / AI agent instructions for the advent-of-code-python repository -->

# How to be productive in this repository (short, specific)

This repo contains per-day Advent of Code solutions under `src/advent_of_code/year_<YYYY>/day_<NN>.py` with test cases under `tests/year_<YYYY>/test_day_<NN>.py` and input files in `inputs/year_<YYYY>/<NN>.dat`.

Follow these concrete rules and patterns when making changes or adding new solutions:

- Entrypoint contract: each day module should expose a function `main(input_file)` which accepts a path to the input file (string) and performs/prints the solution. `scripts/run_day.py` dynamically imports `advent_of_code.year_<year>.day_<NN>` and calls `main(input_file)`.
- Input handling: use `src/advent_of_code/utils/input_handling.py::read_input(f)` to load inputs as a list of stripped lines. Input files live at `inputs/year_<YYYY>/<NN>.dat` and use zero-padded two-digit day names (e.g. `01.dat`).
- Filenames & modules: code files are named `day_01.py`, `day_02.py`, etc. The module import path is `advent_of_code.year_2025.day_01` (note the zero padding in the module filename).
- Tests & pytest: tests are under `tests/year_<YYYY>/test_day_<NN>.py`. The project config (pyproject.toml) sets `pythonpath = "src"` and `--import-mode=importlib`, so prefer importable modules and avoid relying on working-directory-only imports.

Quick commands (examples you can run locally):

- Run one day (example for year 2025 day 1):
  python3 scripts/run_day.py --year 2025 --day 1

- Run all discovered solutions (skips days without input files):
  python3 scripts/run_all_solutions.py

- Generate a new day + test from templates (templates in `scripts/templates`):
  python3 scripts/generate_new_day_skeleton_files_from_templates.py --year 2025 --day 1

- Run tests:
  pytest

Key files to inspect when changing behavior:

- `scripts/run_day.py` — dynamic import + `main(input_file)` invocation. If you change the `main` contract, update this script.
- `scripts/run_all_solutions.py` — discovery logic: scans `src/advent_of_code` for `year_*` directories and filenames matching `day_\d{2}\.py`. It will skip running days with no corresponding `inputs/year_<YYYY>/<NN>.dat` file.
- `src/advent_of_code/utils/input_handling.py` — canonical helpers for reading inputs and parsing simple formats used across days.
- `scripts/generate_new_day_skeleton_files_from_templates.py` and `scripts/templates/*` — used to scaffold new day modules and tests; templates include `{day}` and `{year}` placeholders.
- `pyproject.toml` — pytest configuration (`pythonpath=src`, `--import-mode=importlib`), black formatting, and build backend (hatchling). Use these settings when adding CI or packaging.

Project-specific conventions and gotchas (be precise):

- Zero-padding is significant: day files and input files are named with two-digit zero padding (e.g., `day_01.py` ↔ `01.dat`). `run_day.py` zero-pads the provided `--day` argument.
- `run_all_solutions.py` relies on simple `os.listdir` ordering; do not assume nested directories beyond `src/advent_of_code/year_<YYYY>/`.
- The repo uses `python3` in scripts; local development should use a Python 3.8+ interpreter (pyproject says >=3.8). Black config targets Python 3.9 but code is compatible with 3.8+.
- Tests import the package from `src/` via pytest config. When editing tests or modules, ensure the module path `advent_of_code.year_<YYYY>.day_<NN>` is importable.

Small implementation checklist for a new/updated day module:

1. Create `src/advent_of_code/year_<YYYY>/day_<NN>.py` using templates or follow the `main(input_file)` contract.
2. Add `inputs/year_<YYYY>/<NN>.dat` (zero-padded).
3. Add/verify `tests/year_<YYYY>/test_day_<NN>.py` follows existing test style.
4. Use `utils.read_input` where appropriate to keep input parsing consistent.
5. Run `python3 scripts/run_day.py --year <YYYY> --day <N>` and `pytest`.

If you need to change a project-wide behavior (import rules, test config, discovery), update `pyproject.toml` and the scripts above; prefer small, backward-compatible changes because many scripts dynamically import day modules.

If anything here is unclear or you'd like the instructions to be stricter (for example, enforcing a return value contract instead of printing), tell me which style you'd prefer and I will update this file.
