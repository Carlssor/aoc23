import re


def _read_input_contents(input_filename: str) -> list[str]:
    with open(input_filename, "r") as f:
        contents = f.readlines()
    return contents


def solve(puzzle_input: list[str]) -> int:
    calibration_value = 0
    for line in puzzle_input:
        current_line = re.sub(r"[^0-9]", "", line)
        calibration_value += int(current_line[0] + current_line[-1])
    return calibration_value


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
