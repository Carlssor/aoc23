import unittest

import day02.puzzle1
import day02.puzzle2


class Test(unittest.TestCase):
    def test_game_id(self):
        game_format_string = "Game {}: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        for expected_id in (1, 100, 1337):
            game_string = game_format_string.format(expected_id)
            self.assertEqual(day02.puzzle1._find_game_id(game_string), expected_id)

    def test_find_one_set_of_cubes(self):
        self.assertEqual(
            day02.find_one_set_of_cubes("3 blue, 6 red"),
            {"blue": 3, "red": 6}
        )
        self.assertEqual(
            day02.find_one_set_of_cubes("1 green"),
            {"green": 1}
        )
        self.assertEqual(
            day02.find_one_set_of_cubes("1 green, 2 red, 77 blue"),
            {"green": 1, "red": 2, "blue": 77}
        )

    def test_split_puzzle_input(self):
        self.assertEqual(
            day02.split_puzzle_input(
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"),
            ("Game 3",
             ["8 green, 6 blue, 20 red", "5 blue, 4 red, 13 green", "5 green, 1 red"])
        )

    def test_check_if_possible_cubes(self):
        available_cubes = dict(day02.puzzle1.available_cubes)
        self.assertTrue(day02.puzzle1._check_if_possible_cubes({}))
        cubes_with_one_each = dict((color, 1) for color in available_cubes)
        self.assertTrue(day02.puzzle1._check_if_possible_cubes(cubes_with_one_each))
        self.assertTrue(day02.puzzle1._check_if_possible_cubes(available_cubes))
        for color in available_cubes:
            cubes_with_too_many_of_one_color = dict(available_cubes)
            cubes_with_too_many_of_one_color[color] = cubes_with_too_many_of_one_color[color] + 1
            self.assertFalse(day02.puzzle1._check_if_possible_cubes(cubes_with_too_many_of_one_color))

    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = day02.puzzle1.solve(f.readlines())
        self.assertEqual(result, 8)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = day02.puzzle2.solve(f.readlines())
        self.assertEqual(result, 2286)


if __name__ == "__main__":
    unittest.main()
