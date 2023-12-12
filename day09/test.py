import unittest

from day09 import puzzle1, puzzle2


class Test(unittest.TestCase):
    def test_solve_puzzle_1(self):
        with open("input_example.txt") as f:
            result = puzzle1.solve(f.readlines())
        self.assertEqual(result, 114)

    def test_solve_puzzle_2(self):
        with open("input_example.txt") as f:
            result = puzzle2.solve(f.readlines())
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
