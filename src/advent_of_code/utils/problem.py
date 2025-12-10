from typing import List, Optional, Tuple
from pathlib import Path

from advent_of_code.utils.input_handling import read_input


class Problem:
    """Base class for Advent of Code day modules.

    Subclass this and implement `solve(self, input_lines)` which returns
    a tuple (part1, part2). Subclasses should set YEAR and DAY class attributes.

    This base class provides a `run(input_file)` helper which reads the
    input using the repo's `read_input` helper and prints results in the
    canonical format used across the repo.
    """

    YEAR: Optional[int] = None
    DAY: Optional[int] = None
    title: Optional[str] = None

    def part1(self, input_lines: List[str]) -> Optional[object]:
        """Override in subclasses to implement part 1.

        Args:
            input_lines: list of stripped lines from the day's input file.

        Returns:
            part1 result (or None)
        """
        raise NotImplementedError("Subclasses must implement part1(input_lines)")

    def part2(self, input_lines: List[str]) -> Optional[object]:
        """Override in subclasses to implement part 2.

        Same shape as `part1`.
        """
        raise NotImplementedError("Subclasses must implement part2(input_lines)")

    def solve(self, input_lines: List[str]) -> Tuple[Optional[object], Optional[object]]:
        """Run both parts and return a (part1, part2) tuple.

        This moves the usual `solve` boilerplate into the base class so
        subclasses only need to implement `part1` and `part2`.
        """
        return (self.part1(input_lines), self.part2(input_lines))

    def run(self, input_file: str) -> Tuple[Optional[object], Optional[object]]:
        """Read the input file, run solve, print results and return them.

        Keeps the same `main(input_file)` contract used across the project.
        """
        input_lines = read_input(input_file)
        result_part_1, result_part_2 = self.solve(input_lines)

        day_str = f"{self.DAY:02d}" if isinstance(self.DAY, int) else str(self.DAY)
        print(
            f"Day {day_str} \n"
            f" Result for part 1 is {result_part_1} \n"
            f" Result for part 2 is {result_part_2} \n"
        )

        return (result_part_1, result_part_2)


    @classmethod
    def main(cls, input_file: Optional[str] = None):
        """Construct, run, and return results.

        If `input_file` is None the method will attempt to locate the
        repository's default input file at
        `inputs/year_<YEAR>/<DD>.dat` (matching the project's convention).

        Raises FileNotFoundError if the inferred input file does not exist
        or ValueError if YEAR/DAY are not set on the subclass.
        """
        if input_file is None:
            if cls.YEAR is None or cls.DAY is None:
                raise ValueError(
                    "Either pass input_file or set YEAR and DAY on the Problem subclass"
                )

            # Determine repository root relative to this file: src/advent_of_code/utils/problem.py
            repo_root = Path(__file__).resolve().parents[3]
            candidate = repo_root / "inputs" / f"year_{cls.YEAR}" / f"{cls.DAY:02d}.dat"
            if candidate.exists():
                input_file = str(candidate)
            else:
                raise FileNotFoundError(
                    f"Input file not found at {candidate}. Provide `input_file` explicitly."
                )

        instance = cls()
        return instance.run(input_file)
