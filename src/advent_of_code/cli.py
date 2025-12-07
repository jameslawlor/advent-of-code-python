"""CLI entrypoint for the advent_of_code package.

Provides a small, modern CLI so the project can be run as:

- `python -m advent_of_code --year 2025 --day 1`
- or, after editable install: `aoc --year 2025 --day 1`

This duplicates the behavior of `scripts/run_day.py` but lives inside the package.
"""

from __future__ import annotations

import argparse
import importlib
from typing import Optional, Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Console entry point.

    Args:
        argv: list of args (None -> sys.argv[1:])

    Returns:
        exit code (0 on success).
    """
    parser = argparse.ArgumentParser(
        prog="aoc", description="Run an Advent of Code solution module"
    )
    parser.add_argument(
        "--year", required=True, type=int, help="Year directory (e.g. 2025)"
    )
    parser.add_argument("--day", required=True, type=str, help="Day number (1 or 01)")

    args = parser.parse_args(argv)

    day_zero_padded_str = str(args.day).zfill(2)
    input_file = f"inputs/year_{args.year}/{day_zero_padded_str}.dat"

    day_module = f"advent_of_code.year_{args.year}.day_{day_zero_padded_str}"

    try:
        module = importlib.import_module(day_module)
    except ModuleNotFoundError as exc:
        print(f"Could not find module: {day_module}")
        # Helpful hint: if running from the repository root,
        # make sure `src` is on PYTHONPATH or install the package editable.
        print(
            "Hint: run with `PYTHONPATH=src python -m advent_of_code ...` "
            "or `pip install -e .` to make the package importable"
        )
        if isinstance(exc, ModuleNotFoundError):
            # show original message
            print(str(exc))
        return 1

    if hasattr(module, "main"):
        try:
            module.main(input_file)
            return 0
        except Exception:
            # Bubble up stack trace for debugging convenience
            raise
    else:
        print(f"The module {day_module} does not have a 'main(input_file)' function.")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
