import re


def get_numbers_and_positions(line: str) -> list[tuple[int, str]]:
    result = []
    for match in re.finditer(r"(\d+)", line):
        result.append((match.start(), match.group(1)))
    return result


def get_adjacent_positions(line_number: int, position: int, number_length: int) -> set[tuple[int, int]]:
    adjacent_positions: list[tuple[int, int]] = []
    for current_position in range(position - 1, position + number_length + 1):
        adjacent_positions.extend([(line_number - 1, current_position), (line_number + 1, current_position)])
    adjacent_positions.extend([(line_number, position - 1), (line_number, position + number_length)])
    return set(adjacent_positions)
