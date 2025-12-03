"""Allow running the package with `python -m advent_of_code`.

Example:
  python -m advent_of_code --year 2025 --day 1

This file delegates to `advent_of_code.cli:main`.
"""
from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())
