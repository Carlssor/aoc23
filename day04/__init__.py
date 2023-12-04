import re


def _get_numbers(line: str) -> set[int]:
    return {int(num) for num in line.split()}


def get_played_and_winning_numbers(line: str) -> tuple[set[int], set[int]]:
    match = re.match(r"(.+):(.*)\|(.*)", line)
    played_numbers = _get_numbers(match.group(2))
    winning_numbers = _get_numbers(match.group(3))
    return played_numbers, winning_numbers


def calculate_correct_played_numbers(played_numbers: set[int], winning_numbers: set[int]) -> int:
    return len(played_numbers & winning_numbers)


def calculate_score(played_numbers: set[int], winning_numbers: set[int]) -> int:
    amount_correct_played_numbers = calculate_correct_played_numbers(played_numbers, winning_numbers)
    if amount_correct_played_numbers > 0:
        return 2 ** (amount_correct_played_numbers - 1)
    return 0
