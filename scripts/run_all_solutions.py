import os
import re
import subprocess

BASE_DIR = "src/advent_of_code"
YEARS_DIR = os.path.join(BASE_DIR, "year_")
RUN_DAY_SCRIPT = "scripts/run_day.py"
INPUTS_DIR = "inputs"


def discover_and_run_solutions():
    # Regex to match "day_<number>.py"
    day_pattern = re.compile(r"day_(\d{2})\.py")

    for year in sorted(os.listdir(BASE_DIR)):
        if year.startswith("year_"):
            year_path = os.path.join(BASE_DIR, year)
            year_number = year.split("_")[1]

            # Look for days in the "days" directory
            days_dir = os.path.join(year_path)
            for file in sorted(os.listdir(days_dir)):
                match = day_pattern.match(file)
                if match:
                    day_number = match.group(1)

                    # Build input file path
                    input_file = os.path.join(
                        INPUTS_DIR, f"year_{year_number}", f"{day_number}.dat"
                    )
                    if not os.path.exists(input_file):
                        print(f"Input for {year_number} {day_number} missing, skipping")
                        continue

                    # Run the solution using run_day.py
                    try:
                        print(f"Running {year_number} Day {day_number}...")
                        subprocess.run(
                            [
                                "python3",
                                RUN_DAY_SCRIPT,
                                "--year",
                                year_number,
                                "--day",
                                str(
                                    int(day_number)
                                ),  # Remove leading zero for argument
                            ],
                            check=True,
                        )
                        print("\n")
                    except subprocess.CalledProcessError as e:
                        print(f"Error running {year_number} Day {day_number}: {e}")


if __name__ == "__main__":
    discover_and_run_solutions()
