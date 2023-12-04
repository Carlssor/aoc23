import unittest

import day03.puzzle1
import day03.puzzle2


class Test(unittest.TestCase):
    def test_get_numbers_and_positions(self):
        self.assertEqual(day03.get_numbers_and_positions("1"), [(0, "1")])
        self.assertEqual(day03.get_numbers_and_positions("1.2"), [(0, "1"), (2, "2")])
        self.assertEqual(day03.get_numbers_and_positions("1.2+.+123"), [(0, "1"), (2, "2"), (6, "123")])

    def test_get_symbol_positions_in_line(self):
        self.assertEqual(day03.puzzle1._get_symbol_positions_in_line("*"), [0])
        self.assertEqual(day03.puzzle1._get_symbol_positions_in_line("*.*"), [0, 2])
        self.assertEqual(day03.puzzle1._get_symbol_positions_in_line("1"), [])
        self.assertEqual(day03.puzzle1._get_symbol_positions_in_line("1**123.1*33.."), [1, 2, 8])

    def test_get_adjacent_positions(self):
        self.assertEqual(
            day03.get_adjacent_positions(0, 0, 1),
            {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}
        )
        self.assertEqual(
            day03.get_adjacent_positions(0, 0, 2),
            {(-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -1), (0, 2), (1, -1), (1, 0), (1, 1), (1, 2)}
        )

    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = day03.puzzle1.solve(f.readlines())
        self.assertEqual(result, 4361)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = day03.puzzle2.solve(f.readlines())
        self.assertEqual(result, 467835)


if __name__ == "__main__":
    unittest.main()
