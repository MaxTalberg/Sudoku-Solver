"""
PROTOTYPING

read_board_from_file(filename):

    Read the Sudoku puzzle from input or define it as a 2D array.

Unit testing:

    - Test with non-existent file: no file present *DONE*
    - Test with invalid file: no puzzle string *DONE*
    - Test with valid file: valid puzzle string
        of 81 characters *DONE*
    - Test with solvable board: solvable board
        with one known solution *DONE*
    - Test with unsolvable board: impossible board
        with no solution
    - Test with empty board: empty unsolved board
    - Test with solved board: full solved board
    - Test with invalid board size: board not
        81 characters in length *DONE*
    - Test with invalid characters: puzzle string
        contains invalid characters *DONE*
    - Test with true (valid, duplicates, ect)
        values: row, column and 3x3 square
    - Test with false (invalid, dupilcates, ect)
        values: row, column and 3x3 square
    - Test with multiple solutions: board
        with multiple solutions

"""
import sys

# import numpy as np


class SudokuSolver:
    """Class to solve a sudoku"""

    # initialise board from file
    def __init__(self, filename):
        """
        Initialises the sudoku board
        """
        try:
            self.board = self.read_board_from_file(filename)
        except (FileNotFoundError, ValueError) as error:
            raise RuntimeError(f"Failed to initialise board: {error}")

    def read_board_from_file(self, filename):
        """
        Reads a sudoku puzzle from a text file
        and converts it into a list of lists where
        each sublist represents a row of the sudoku

        Parameters
        ----------
        filename: str
            numbers for the initial sudoku board

        Returns
        ----------
        list(int)
            A list of lists representing each row
            of the initial sudoko board

        """

        # Initialise the empty board
        board = []

        with open(filename, "r") as file:
            for line_number, line in enumerate(file, 1):
                # Ignore the grid separators
                if line.startswith("---"):
                    continue

                # Remove the grid dividers and newline characters
                # then split into numbers
                row = line.replace("|", "").replace("\n", "")

                # validate row length
                if len(row) != 9:
                    raise ValueError(f"Row length is not 9 at {line_number}")

                # Convert each character to an integer
                try:
                    row_numbers = [int(char) for char in row]

                    # validate numbers are between 0 and 9
                    if any(n < 0 or n > 9 for n in row_numbers):
                        raise ValueError("Invalid number found in row")

                    # validate there are no duplicates in rows
                    non_zero_row_vals = [
                        number for number in row_numbers if number != 0
                    ]
                    if len(set(non_zero_row_vals)) != len(non_zero_row_vals):
                        raise ValueError("Duplicate number found in row")

                except ValueError:
                    # if the character is not an integer
                    raise ValueError("Invalid character found")

                # append row to board
                board.append(row_numbers)

        # validate board size
        if len(board) != 9:
            raise ValueError("Board size is not 9 x 9")

        # validate there are no duplicates in columns
        for col in range(len(board[0])):
            non_zero_col_vals = [
                board[row][col]
                for row in range(len(board))
                if board[row][col] != 0
            ]
            if len(set(non_zero_col_vals)) != len(non_zero_col_vals):
                raise ValueError("Duplicate number found in column")

        # validate there are no duplicates in 3x3 squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                non_zero_square_vals = [
                    board[row + i][col + j]
                    for i in range(3)
                    for j in range(3)
                    if board[row + i][col + j] != 0
                ]
                if len(set(non_zero_square_vals)) != len(non_zero_square_vals):
                    raise ValueError("Duplicate number found in 3x3 square")

        # validate board is not empty
        if sum(sum(board, [])) == 0:
            raise ValueError("Board is empty!")

        # validate board is not full
        if sum(sum(board, [])) == (45 * 9):
            raise ValueError("Board is already full!")

        # Return the matrix of the inserted sudoku board
        return board

    def check_possible_indicies(self, x, y, n):
        """
        Checks if a certain indicies is possible
        on a certain grid of the sudoku board

        Parameters
        ----------
        board: list(list(int))
            The current state of the sudoku board

        x: int
            Column number of the sudoku board

        y: int
            Row number of the sudoku board

        n: int
            indicie to check in the grid square

        Returns
        ----------
        Boolean
            True if number is allowed, False otherwise
        """
        if self.board is None:
            return False

        # checks if n is in column x or row y
        for i in range(0, 9):
            if self.board[i][x] == n or self.board[y][i] == n:
                return False

        # top left corner of 3x3 square
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3

        # checks if n is in 3x3 square
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[y0 + i][x0 + j] == n:
                    return False

        # return True if intiger is allowed on square x, y
        return True

    def solve_sudoku(self):
        """
        Solves the sudoku by recurssion of
        possbile indicies

        Parameters
        ----------
        board: list(list(int))
            The current state of the sudoku board

        Returns
        ----------
        board: list(list(int))
            The solved sudoku board

        """
        if self.board is None:
            # print("Error: No board found")
            return None
        # checks if square is blank, contains a 0
        for x in range(9):
            for y in range(9):
                if self.board[y][x] == 0:
                    # check if number n can be here
                    for n in range(1, 10):
                        if self.check_possible_indicies(x, y, n):
                            self.board[y][x] = n
                            if self.solve_sudoku():
                                return self.board
                            # backtracking!
                            self.board[y][x] = 0
                    return None
        # returns board when a solution is found
        return self.board

    def get_board(self):
        """
        Provides current state of the sudoku board

        Returns
        ----------
        board: list(list(int))
            The current state of the sudoku board

        """
        return self.board


def main():
    # Check the correct number of command line arguements are passsed
    if len(sys.argv) != 2:
        # print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return

    # input file containing sudoku
    input_file = sys.argv[1]

    # initial unsolved sudoku
    sododku_solver = SudokuSolver(input_file)
    # print("\nInitial unsolved sudoku: \n\n")
    # print(np.matrix(sododku_solver.get_board())))

    # final solved sudoku
    sododku_solver.solve_sudoku()
    # print("\nFinal solved sudoku: \n\n")
    # print(np.matrix(sododku_solver.get_board())))
    return


if __name__ == "__main__":
    main()
