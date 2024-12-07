import importlib
import sys

# if len(sys.argv) < 2:
#     print("Usage: python run_day.py <day>")
#     sys.exit(1)

day = sys.argv[1]

try:
    module = importlib.import_module(f"advent_of_code.year_2023.days.{day}")
    module.main()  # Assumes each day's file has a `main` function
except ModuleNotFoundError:
    print(f"Day {day} not found.")
