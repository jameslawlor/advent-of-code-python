import importlib
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run a specific Advent of Code solution.")
    # parser.add_argument(
    #     "--input_file", 
    #     required=True, 
    #     type=str, 
    #     help="Path to the input file for the day's solution."
    # )
    parser.add_argument(
        "--year", 
        required=True, 
        type=int, 
    )
    parser.add_argument(
        "--day", 
        required=True, 
        type=str, 
    )

    args = parser.parse_args()
    day_zero_padded_str = str(args.day).zfill(2)
    input_file = f"inputs/year_{args.year}/{day_zero_padded_str}.dat"

    day_module = f"advent_of_code.year_{args.year}.day_{day_zero_padded_str}"

    try:
        # Dynamically import the module for the specified day
        module = importlib.import_module(day_module)
        # Run the solution (assumes each solver module has a `main()` function)
        if hasattr(module, "main"):
            module.main(input_file)
        else:
            print("man")
            print(f"The module {day_module} does not have a 'main(input_file)' function.")
    except ModuleNotFoundError:
        print(f"Could not find module: {day_module}")
        sys.exit(1)

if __name__ == "__main__":
    main()
