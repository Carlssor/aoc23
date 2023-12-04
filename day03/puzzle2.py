import math

import day03


def _get_gear_symbol_positions_in_line(line: str) -> list[int]:
    return [pos for pos in range(len(line.strip())) if line[pos] == "*"]


def solve(puzzle_input: list[str]) -> int:
    result = 0
    numbers_and_positions: list[tuple[int, int, str]] = []
    gear_symbols: dict[tuple[int, int], list[int]] = {}
    for line_number, line in enumerate(puzzle_input):
        numbers_and_positions.extend(
            [(line_number, position, number) for (position, number) in day03.get_numbers_and_positions(line)])
        for gear_symbol_position in _get_gear_symbol_positions_in_line(line):
            gear_symbols[(line_number, gear_symbol_position)] = []
    for line_number, position, number in numbers_and_positions:
        adjacent_positions = day03.get_adjacent_positions(line_number, position, len(number))
        for adjacent_position in adjacent_positions:
            gear_list = gear_symbols.get(adjacent_position)
            if gear_list is not None:
                gear_list.append(int(number))
    for gear_symbol in gear_symbols.values():
        if len(gear_symbol) == 2:
            result += math.prod(gear_symbol)
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
