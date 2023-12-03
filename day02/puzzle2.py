import math

import day02


def solve(puzzle_input: list[str]) -> int:
    result = 0
    for game in puzzle_input:
        game_required_cubes = {}
        cube_strings = day02.split_puzzle_input(game)[1]
        for cube_string in cube_strings:
            cubes = day02.find_one_set_of_cubes(cube_string)
            for color, amount in cubes.items():
                game_required_cubes[color] = max(game_required_cubes.get(color, 0), amount)
        result += math.prod(game_required_cubes.values())
    return result


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.readlines()))
