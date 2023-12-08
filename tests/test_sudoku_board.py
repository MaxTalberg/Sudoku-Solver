import unittest
import warnings
from src.sudoku_reader import SudokuReader
from src.sudoku_board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    """
    Test cases for the SudokuBoard class

    The SudokuBoard class is responsible for verifying the sudoku board from
    an array.

    These tests ensure the class handles various validation and array
    scenarios correctly.
    """

    def test_raise_error_for_invalid_file(self):
        """
        Test that the SudokuBoard class raises
        a ValueError when the file is invalid
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_board.txt")
            SudokuBoard(reader.board)

    def test_read_board_from_file_valid(self):
        """
        Test that the SudokuBoard class reads
        a valid board correctly
        """
        reader = SudokuReader("data/valid_board.txt")
        board = SudokuBoard(reader.board)

        expected_board = [
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 0, 9, 5, 0, 4],
            [0, 0, 0, 0, 5, 0, 1, 6, 9],
            [0, 8, 0, 0, 0, 0, 3, 0, 5],
            [0, 7, 5, 0, 0, 0, 2, 9, 0],
            [4, 0, 6, 0, 0, 0, 0, 8, 0],
            [7, 6, 2, 0, 8, 0, 0, 0, 0],
            [1, 0, 3, 9, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(board.board, expected_board)

    def test_raise_error_for_invalid_size_board(self):
        """
        Test that the SudokuBoard class raises a
        ValueError when the sudoku board is not 9x9
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_size_board.txt")
            SudokuBoard(reader.board)

    def test_raise_error_for_invalid_characters_board(self):
        """
        Test that the SudokuBoard class raises a ValueError
        when the sudoku board contains invalid characters
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_characters_board.txt")
            SudokuBoard(reader.board)

    def test__raise_error_for_invalid_row_board(self):
        """
        Test that the SudokuBoard class raises a ValueError
        when the sudoku board contains a row with duplicate values
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_row_board.txt")
            SudokuBoard(reader.board)

    def test__raise_error_for_invalid_column_board(self):
        """
        Test that the SudokuBoard class raises a ValueError
        when the sudoku board contains a column with duplicate values
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_column_board.txt")
            SudokuBoard(reader.board)

    def test__raise_error_for_invalid_square_board(self):
        """
        Test that the SudokuBoard class raises a ValueError
        when the sudoku board contains a 3x3 square with duplicate values
        """
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_square_board.txt")
            SudokuBoard(reader.board)

    def test_warning_for_empty_board(self):
        """
        Test that the SudokuBoard class raises a warning
        when the sudoku board is empty
        """
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            reader = SudokuReader("data/empty_board.txt")
            _ = SudokuBoard(reader.board)
            self.assertIn("Warning: Board is empty", str(w[-1].message))

    def test_warning_for_less_than_17_starting_values(self):
        """
        Test that the SudokuBoard class raises a warning
        when the sudoku board contains less than 17 starting values
        as this could result in multiple solutions
        """
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            reader = SudokuReader("data/less_than_17_board.txt")
            _ = SudokuBoard(reader.board)
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "Warning: Board has less than 17 starting values. "
            "May have multiple solutions." in str(w[-1].message)


if __name__ == "__main__":
    unittest.main()
