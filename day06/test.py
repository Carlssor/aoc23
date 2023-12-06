import unittest

import day06.puzzle1
import day06.puzzle2


class Test(unittest.TestCase):
    def test_puzzle1_parse_time_and_distance(self):
        self.assertEqual(
            day06.puzzle1.parse_time_and_distance(["Time: 1 2", "Distance: 23 1337"]),
            [(1, 23), (2, 1337)]
        )

    def test_puzzle2_parse_time_and_distance(self):
        self.assertEqual(
            day06.puzzle2.parse_time_and_distance(["Time: 1 2", "Distance: 23 1337"]),
            (12, 231337)
        )

    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = day06.puzzle1.solve(f.readlines())
        self.assertEqual(result, 288)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = day06.puzzle2.solve(f.readlines())
        self.assertEqual(result, 71503)


if __name__ == "__main__":
    unittest.main()
