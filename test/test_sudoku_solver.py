print("#####\n#####\n####")
import unittest
from src.sudoku_solver import SudokuSolver


class TestSudokuSolver(unittest.TestCase):
    """
    Read the Sudoku puzzle from input or define it as a 2D array.
    Unit testing
    - Test with non-existent file: no file present
    - Test with invalid file: no puzzle string
    - Test with valid file: valid puzzle string of 81 characters
    - Test with solvable board: solvable board with one known solution
    - Test with unsolvable board: impossible board with no solution
    - Test with empty board: empty unsolved board
    - Test with solved board: full solved board
    - Test with invalid board size: board not 81 characters in length
    - Test with invalid characters: puzzle string contains invalid characters
    - Test with true (valid) values: row, column and 3x3 square
    - Test with false (invalid) values: row, column and 3x3 square
    """

    # test with non-existent file
    def test_non_existent_file(self):
        solver = SudokuSolver("non_existent_file.txt")
        assert solver.puzzle == None
        pass

    # test with invalid file
    def test_read_board_from_invalid_file(self):
        solver = SudokuSolver("invalid_file.txt")
        assert solver.puzzle == None
        pass

    # test with valid file
    def test_read_board_from_file_valid(self):
        solver = SudokuSolver("valid_file.txt")
        expected_board = [
            [
                0,
                0,
                0,
                0,
                0,
                7,
                0,
                0,
                0,
            ],
            [0, 0, 0, 0, 0, 9, 5, 0, 4],
            [0, 0, 0, 0, 5, 0, 1, 6, 9],
            [0, 8, 0, 0, 0, 0, 3, 0, 5],
            [0, 7, 5, 0, 0, 0, 2, 9, 0],
            [4, 0, 6, 0, 0, 0, 0, 8, 0],
            [7, 6, 2, 0, 8, 0, 0, 0, 0],
            [1, 0, 3, 9, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
        ]
        assert solver.get_board() == expected_board
        pass

    # test with solvable board
    def test_solve_sudoku_solvable(self):
        solver = SudokuSolver("valid_file.txt")
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
        assert solver.solve_sudoku() == expected_board
        pass

    # test with unsolvable board
    def test_solve_sudoku_unsolvable(self):
        solver = SudokuSolver("unsolvable_file.txt")
        assert solver.solve_sudoku() == None
        pass

    # test with empty board
    def test_solve_sudoku_empty(self):
        solver = SudokuSolver("empty_file.txt")
        assert solver.solve_sudoku() == None
        pass

    # test with solved board
    def test_solve_sudoku_solved(self):
        solver = SudokuSolver("solved_file.txt")
        assert solver.solve_sudoku() == None
        pass

    # test with invalid board size
    def test_solve_sudoku_invalid_size(self):
        solver = SudokuSolver("invalid_size_file.txt")
        assert solver.solve_sudoku() == None
        pass

    # test with invalid characters
    def test_solve_sudoku_invalid_characters(self):
        solver = SudokuSolver("invalid_characters_file.txt")
        assert solver.solve_sudoku() == None
        pass

    # test with true values
    def test_check_possible_indicies_true(self):
        solver = SudokuSolver("valid_file.txt")
        assert solver.check_possible_indicies(0, 0, 0) == True
        assert solver.check_possible_indicies(1, 1, 0) == True
        assert solver.check_possible_indicies(2, 2, 0) == True
        assert solver.check_possible_indicies(3, 3, 0) == True
        assert solver.check_possible_indicies(4, 4, 0) == True
        assert solver.check_possible_indicies(5, 5, 0) == True
        assert solver.check_possible_indicies(6, 6, 0) == True
        assert solver.check_possible_indicies(7, 7, 0) == True
        assert solver.check_possible_indicies(8, 8, 0) == True
        pass

    # test with false values
    def test_check_possible_indicies_edge(self):
        solver = SudokuSolver("valid_file.txt")
        assert solver.check_possible_indicies(0, 0, 5) == False
        assert solver.check_possible_indicies(0, 0, 0) == False
        assert solver.check_possible_indicies(0, 8, 0) == False
        assert solver.check_possible_indicies(8, 0, 0) == False
        assert solver.check_possible_indicies(8, 8, 0) == False
        pass

    # test edge cases
    def test_edge_cases(self):
        pass


if __name__ == "__main__":
    unittest.main()
