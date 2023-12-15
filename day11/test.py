import unittest

from day11 import puzzle1, puzzle2


class Test(unittest.TestCase):
    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = puzzle1.solve([line.strip() for line in f.readlines()])
        self.assertEqual(result, 374)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = puzzle2.solve([line.strip() for line in f.readlines()])
        self.assertEqual(result, 82000210)


if __name__ == "__main__":
    unittest.main()
