import day03


def _get_symbol_positions_in_line(line: str) -> list[int]:
    return [pos for pos in range(len(line.strip())) if line[pos] not in ".0123456789"]


def solve(puzzle_input: list[str]) -> int:
    result = 0
    numbers_and_positions: list[tuple[int, int, str]] = []
    symbol_positions: set[tuple[int, int]] = set()
    for line_number, line in enumerate(puzzle_input):
        numbers_and_positions.extend(
            [(line_number, position, number) for (position, number) in day03.get_numbers_and_positions(line)])
        symbol_positions.update(
            {(line_number, symbol_position) for symbol_position in _get_symbol_positions_in_line(line)})
    for line_number, position, number in numbers_and_positions:
        adjacent_positions = day03.get_adjacent_positions(line_number, position, len(number))
        if len(adjacent_positions & symbol_positions) > 0:
            result += int(number)
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
