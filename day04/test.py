import unittest

import day04.puzzle1
import day04.puzzle2


class Test(unittest.TestCase):
    def test_get_numbers(self):
        self.assertEqual(
            day04.get_played_and_winning_numbers("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"),
            ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}))

    def test_calculate_correct_played_numbers(self):
        self.assertEqual(day04.calculate_correct_played_numbers({1}, set()), 0)
        self.assertEqual(day04.calculate_correct_played_numbers({1}, {2}), 0)
        self.assertEqual(day04.calculate_correct_played_numbers({1}, {1, 2}), 1)
        self.assertEqual(day04.calculate_correct_played_numbers({1, 2}, {1}), 1)
        self.assertEqual(day04.calculate_correct_played_numbers({1, 2, 3}, {1, 2, 4}), 2)
        self.assertEqual(day04.calculate_correct_played_numbers({1, 2, 3, 4, 5}, {1, 2, 3, 4, 6}), 4)

    def test_calculate_score(self):
        self.assertEqual(day04.calculate_score({1}, set()), 0)
        self.assertEqual(day04.calculate_score({1}, {2}), 0)
        self.assertEqual(day04.calculate_score({1}, {1, 2}), 1)
        self.assertEqual(day04.calculate_score({1, 2}, {1}), 1)
        self.assertEqual(day04.calculate_score({1, 2, 3}, {1, 2, 4}), 2)
        self.assertEqual(day04.calculate_score({1, 2, 3, 4, 5}, {1, 2, 3, 4, 6}), 8)

    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = day04.puzzle1.solve(f.readlines())
        self.assertEqual(result, 13)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = day04.puzzle2.solve(f.readlines())
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()
