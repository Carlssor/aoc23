import re


def find_one_set_of_cubes(cubes_string: str) -> dict[str, int]:
    result = {}
    for cube_string in cubes_string.split(","):
        cube_string = cube_string.strip()
        match = re.match(r"(\d+) (blue|red|green)", cube_string)
        amount, cube_color = match.groups()
        result[cube_color] = int(amount)
    return result


def split_puzzle_input(puzzle_input: str) -> tuple[str, list[str]]:
    game_id_string, cube_string = puzzle_input.split(":")
    cube_strings = [part.strip() for part in cube_string.split(";")]
    return game_id_string.strip(), cube_strings
