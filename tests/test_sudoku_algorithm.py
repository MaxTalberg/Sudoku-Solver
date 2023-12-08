import unittest
from src.sudoku_reader import SudokuReader
from src.sudoku_board import SudokuBoard
from src.sudoku_algorithm import SudokuAlgorithm


class TestSudokuAlgorithm(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
