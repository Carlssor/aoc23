import unittest

import day07.puzzle1
import day07.puzzle2


class Test(unittest.TestCase):
    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = day07.puzzle1.solve(f.readlines())
        self.assertEqual(result, 6440)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = day07.puzzle2.solve(f.readlines())
        self.assertEqual(result, 5905)


if __name__ == "__main__":
    unittest.main()
