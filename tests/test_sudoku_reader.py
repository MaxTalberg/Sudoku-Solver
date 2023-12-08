import unittest
from src.sudoku_reader import SudokuReader


class TestSudokuReader(unittest.TestCase):
    """
    Test cases for the SudokuReader class

    The SudokuReader class is responsible for reading
    a sudoku board for a given file.

    These tests ensure the class handles various file
    input scenarios correctly.
    """

    def test_non_existent_file(self):
        """
        Test that the SudokuReader class raises
        a RuntimeError when the file does not exist
        """
        with self.assertRaises(RuntimeError):
            SudokuReader("data/non_existent_file.txt")

    def test_solve_sudoku_empty_text_file(self):
        """
        Test that the SudokuReader class raises
        a ValueError when the file is empty
        """
        with self.assertRaises(RuntimeError):
            SudokuReader("data/empty_file.txt")

    def test_not_a_text_file(self):
        """
        Test that the SudokuReader class raises
        a RuntimeError when the file is not a text file
        """
        with self.assertRaises(RuntimeError):
            SudokuReader("data/not_a_text_file.pdf")


if __name__ == "__main__":
    unittest.main()
