from utils import find_galaxy_positions


def _expand_image(puzzle_input: list[str]) -> list[str]:
    image = []
    for line in puzzle_input:
        line = list(line)
        image.append(line)
        if "#" not in line:
            image.append(list(line))
    col = 0
    while col < len(image[0]):
        if all(line[col] == "." for line in image):
            for insert_line in image:
                insert_line.insert(col, ".")
            col += 1
        col += 1
    return ["".join(line) for line in image]


def _calculate_distance(position1: tuple[int, int], position2: tuple[int, int]) -> int:
    return sum(abs(pos1 - pos2) for (pos1, pos2) in zip(position1, position2))


def solve(puzzle_input: list[str]) -> int:
    result = 0
    image = _expand_image(puzzle_input)
    positions = find_galaxy_positions(image)
    for galaxy1_index, galaxy1_position in enumerate(positions):
        for galaxy2_position in positions[galaxy1_index: ]:
            result += _calculate_distance(galaxy1_position, galaxy2_position)
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve([line.strip() for line in f.readlines()]))
