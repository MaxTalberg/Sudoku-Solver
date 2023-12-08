import unittest
import warnings
from src.sudoku_reader import SudokuReader
from src.sudoku_board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    # test with invalid file
    def test_read_board_from_invalid_file(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_file.txt")
            SudokuBoard(reader.board)
            pass

    # test with valid file
    def test_read_board_from_file_valid(self):
        reader = SudokuReader("data/valid_file.txt")
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
        pass

    # test with invalid board size
    def test_solve_sudoku_invalid_size(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_size_file.txt")
            SudokuBoard(reader.board)

    # test with invalid characters
    def test_solve_sudoku_invalid_characters(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_characters_file.txt")
            SudokuBoard(reader.board)

        # test with invalid row

    def test_indicies_invalid_row(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_row_file.txt")
            SudokuBoard(reader.board)

    # test with invalid column
    def test_indicies_invalid_column(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_column_file.txt")
            SudokuBoard(reader.board)

    # test with invalid 3x3 square
    def test_indicies_invalid_square(self):
        with self.assertRaises(ValueError):
            reader = SudokuReader("data/invalid_square_file.txt")
            SudokuBoard(reader.board)

        # test with empty text file

    def test_solve_sudoku_empty_text_file(self):
        with self.assertRaises(ValueError):
            reader = SudokuBoard("data/empty_file.txt")
            SudokuBoard(reader.board)

        # warning less than 17 starting values

    def test_board_less_than_17_starting_values(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            # not to trigger flake8 warning
            reader = SudokuReader("data/less_than_17_board.txt")
            _ = SudokuBoard(reader.board)
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "Board has less than 17 starting values" in str(
                w[-1].message
            )
            pass


if __name__ == "__main__":
    unittest.main()
