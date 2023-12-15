from utils import find_galaxy_positions


def _calculate_space_sizes(image: list[str]) -> list[list[int]]:
    space_expansion_factor = 1000000
    space_sizes = [[1] * len(image[0]) for _ in range(len(image))]
    for row, line in enumerate(image):
        if "#" not in line:
            for col in range(len(line)):
                space_sizes[row][col] *= space_expansion_factor
    for col in range(len(image[0])):
        if all(line[col] == "." for line in image):
            for row in range(len(image)):
                space_sizes[row][col] *= space_expansion_factor
    return space_sizes


def _calculate_distance(position1: tuple[int, int], position2: tuple[int, int], sizes: list[list[int]]) -> int:
    distance = 0
    start_row, end_row = (position1[0], position2[0]) if position2[0] > position1[0] else (position2[0], position1[0])
    start_col, end_col = (position1[1], position2[1]) if position2[1] > position1[1] else (position2[1], position1[1])
    for col in range(start_col + 1, end_col + 1):
        distance += sizes[start_row][col]
    for row in range(start_row + 1, end_row + 1):
        distance += sizes[row][start_col]
    return distance


def solve(puzzle_input: list[str]) -> int:
    result = 0
    positions = find_galaxy_positions(puzzle_input)
    sizes = _calculate_space_sizes(puzzle_input)
    for galaxy1_index, galaxy1_position in enumerate(positions):
        for galaxy2_position in positions[galaxy1_index:]:
            result += _calculate_distance(galaxy1_position, galaxy2_position, sizes)
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve([line.strip() for line in f.readlines()]))
