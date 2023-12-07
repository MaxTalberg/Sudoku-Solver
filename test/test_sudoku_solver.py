import unittest
import warnings
from src.sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    # test with non-existent file
    def test_non_existent_file(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/non_existent_file.txt")
            assert solver.puzzle is None
            pass

    # test with invalid file
    def test_read_board_from_invalid_file(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_file.txt")
            assert solver.puzzle is None
            pass

    # test with valid file
    def test_read_board_from_file_valid(self):
        solver = SudokuSolver("data/valid_file.txt")
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
        self.assertEqual(solver.board, expected_board)
        pass

    # test with solvable board
    def test_solve_sudoku_solvable(self):
        solver = SudokuSolver("data/valid_file.txt")
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
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_size_file.txt")
            assert solver.solve_sudoku() is None
            pass

    # test with invalid characters
    def test_solve_sudoku_invalid_characters(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_characters_file.txt")
            assert solver.solve_sudoku() is None
            pass

    # test with true and false values
    def test_check_possible_indicies_true(self):
        solver = SudokuSolver("data/valid_file.txt")
        # check if number n cannot be here
        assert solver.check_possible_indicies(0, 0, 7) is False
        assert solver.check_possible_indicies(1, 1, 9) is False
        assert solver.check_possible_indicies(2, 2, 5) is False
        assert solver.check_possible_indicies(3, 3, 3) is False
        # check if number n can be here
        assert solver.check_possible_indicies(0, 8, 5) is True
        assert solver.check_possible_indicies(8, 0, 3) is True
        assert solver.check_possible_indicies(8, 8, 3) is True
        assert solver.check_possible_indicies(4, 4, 3) is True
        pass

    # test with invalid row
    def test_indicies_invalid_row(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_row_file.txt")
            self.assertFalse(solver.solve_sudoku())
            pass

    # test with invalid column
    def test_indicies_invalid_column(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_column_file.txt")
            self.assertFalse(solver.solve_sudoku())
            pass

    # test with invalid 3x3 square
    def test_indicies_invalid_square(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/invalid_square_file.txt")
            self.assertFalse(solver.solve_sudoku())
            pass

    # test with empty text file
    def test_solve_sudoku_empty_text_file(self):
        with self.assertRaises(RuntimeError):
            solver = SudokuSolver("data/empty_text_file.txt")
            assert solver.solve_sudoku() is None
            pass

    # warning less than 17 starting values
    def test_board_less_than_17_starting_values(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            # not to trigger flake8 warning
            _ = SudokuSolver("data/less_than_17_board.txt")
            assert len(w) == 1
            assert issubclass(w[-1].category, UserWarning)
            assert "Board has less than 17 starting values" in str(
                w[-1].message
            )
            pass


if __name__ == "__main__":
    unittest.main()
