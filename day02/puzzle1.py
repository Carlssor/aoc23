import re

import day02


available_cubes = {"red": 12, "green": 13, "blue": 14}


def _find_game_id(game_string: str) -> int:
    match = re.match(r"Game (\d+)", game_string)
    return int(match.group(1))


def _check_if_possible_cubes(game_cubes: dict[str, int]) -> bool:
    for color, amount in game_cubes.items():
        if available_cubes[color] < amount:
            return False
    return True


def solve(puzzle_input: list[str]) -> int:
    result = 0
    for game in puzzle_input:
        game_id_string, cube_strings = day02.split_puzzle_input(game)
        game_id = _find_game_id(game_id_string)
        for cube_string in cube_strings:
            cubes = day02.find_one_set_of_cubes(cube_string)
            if not _check_if_possible_cubes(cubes):
                break
        else:
            result += game_id
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
