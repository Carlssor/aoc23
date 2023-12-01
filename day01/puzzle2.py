_substitutions = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def _find_first_number(text: str) -> str:
    for position in range(len(text)):
        for possible_substitution, value in _substitutions.items():
            if text[position:].startswith(possible_substitution):
                return value
            elif text[position].isdigit():
                return text[position]


def _find_last_number(text: str) -> str:
    for position in range(len(text) - 1, -1, -1):
        for possible_substitution, value in _substitutions.items():
            if text[: position].endswith(possible_substitution):
                return value
            elif text[position].isdigit():
                return text[position]


def solve(puzzle_input: list[str]) -> int:
    calibration_value = 0
    for line in puzzle_input:
        current_number_text = _find_first_number(line) + _find_last_number(line)
        calibration_value += int(current_number_text)
    return calibration_value


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
