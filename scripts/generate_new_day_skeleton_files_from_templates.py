import argparse
import os

TEMPLATES_PATH = os.path.join("scripts", "templates")


def parse_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=str, required=True)
    parser.add_argument("--year", type=str, required=True)
    args = parser.parse_args()
    return args


def read_template(template_file_path) -> None:
    with open(template_file_path, "r") as template_file:
        return template_file.read()


def write_template(template: str, write_path: str) -> None:
    # if os.path.exists(write_path):
    #     print(f"File {write_path} already exists! Not writing.")
    # else:
    with open(write_path, "w") as f:
        f.write(template)


def generate_file(template_file_path, input_day, input_year, output_file_path):
    try:
        # Read the template content from the file
        template_content = read_template(template_file_path)
    except FileNotFoundError:
        print(f"Template file '{template_file_path}' not found.")
        exit(1)

    # Replace placeholder with the provided integer input
    modified_content = template_content.replace("{day}", str(input_day)).replace(
        "{year}", str(input_year)
    )
    # Generate the Python file from the template
    write_template(modified_content, output_file_path)
    print(f"Python file '{output_file_path}' generated successfully.")


if __name__ == "__main__":
    args = parse_input_args()
    input_day_raw = args.day
    input_year = args.year
    input_day = str(input_day_raw).zfill(2)

    day_file_dest = os.path.join(
        "src", "advent_of_code", f"year_{input_year}", f"day_{input_day}.py"
    )
    template_path = os.path.join(TEMPLATES_PATH, "days_template.txt")
    generate_file(template_path, input_day, input_year, day_file_dest)

    tests_file_dest = os.path.join(
        "tests", f"year_{input_year}", f"test_day_{input_day}.py"
    )
    template_path = os.path.join(TEMPLATES_PATH, "tests_template.txt")
    generate_file(template_path, input_day, input_year, tests_file_dest)
