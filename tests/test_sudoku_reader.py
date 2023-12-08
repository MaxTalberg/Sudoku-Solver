import unittest
from src.sudoku_reader import SudokuReader


class TestSudokuReader(unittest.TestCase):
    # test with non-existent file
    def test_non_existent_file(self):
        with self.assertRaises(RuntimeError):
            SudokuReader("data/non_existent_file.txt")
            pass


if __name__ == "__main__":
    unittest.main()
