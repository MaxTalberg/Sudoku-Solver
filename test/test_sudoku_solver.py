import unittest
import warnings
from src.sudoku_reader import SudokuReader
from src.sudoku_board import SudokuBoard
from src.sudoku_algorithm import SudokuAlgorithm


class TestSudokuSolver(unittest.TestCase):
    # test with non-existent file
    def test_non_existent_file(self):
        with self.assertRaises(RuntimeError):
            SudokuReader("data/non_existent_file.txt")
            pass

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

    # test with solvable board
    def test_solve_sudoku_solvable(self):
        reader = SudokuReader("data/valid_file.txt")
        board = SudokuBoard(reader.board)
        solver = SudokuAlgorithm(board.board)
        expected_board = [
            [5, 9, 4, 1, 6, 7, 8, 3, 2],
            [6, 1, 8, 2, 3, 9, 5, 7, 4],
            [2, 3, 7, 4, 5, 8, 1, 6, 9],
            [9, 8, 1, 7, 2, 6, 3, 4, 5],
            [3, 7, 5, 8, 4, 1, 2, 9, 6],
            [4, 2, 6, 3, 9, 5, 7, 8, 1],
            [7, 6, 2, 5, 8, 4, 9, 1, 3],
            [1, 4, 3, 9, 7, 2, 6, 5, 8],
            [8, 5, 9, 6, 1, 3, 4, 2, 7],
        ]
        # switched solved to True, check solves puzzle
        self.assertTrue(solver.solve_sudoku())

        # check if board matches expected board
        self.assertEqual(solver.board, expected_board)
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

    # test with true and false values
    def test_check_possible_indicies_true(self):
        reader = SudokuReader("data/valid_file.txt")
        board = SudokuBoard(reader.board)
        solver = SudokuAlgorithm(board.board)

        # check if number n cannot be here
        self.assertFalse(solver.check_possible_indicies(0, 0, 7))
        self.assertFalse(solver.check_possible_indicies(1, 1, 9))
        self.assertFalse(solver.check_possible_indicies(2, 2, 5))
        self.assertFalse(solver.check_possible_indicies(3, 3, 3))

        # check if number n can be here
        self.assertTrue(solver.check_possible_indicies(0, 8, 5))
        self.assertTrue(solver.check_possible_indicies(8, 0, 3))
        self.assertTrue(solver.check_possible_indicies(8, 8, 3))
        self.assertTrue(solver.check_possible_indicies(4, 4, 3))
        pass

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
            SudokuBoard("data/invalid_square_file.txt")

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
