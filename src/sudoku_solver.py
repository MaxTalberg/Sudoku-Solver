"""
PROTOTYPING

read_board_from_file(filename):
Unit testing
- Test with non-existent file
- Test with badly formatted file
- Test with correct file


check_possible_indicies(board, x, y, n):
Unit testing
- Test with true values
- Test with false values columnn and row and 3x3 square
- Test edge cases

solve_sudoku(board):
- Test solvable board
- Test solved board
- Test unsolvable board
- Test empty board
- Test invalid board size
based on the validity of the function above.

"""
import sys
import numpy as np


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
            print("Error: ".format(error))
            self.board = None

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
            for line in file:
                # Ignore the grid separators
                if line.startswith("---"):
                    continue

                # Remove the grid dividers and newline characters, then split into numbers
                row = line.replace("|", "").replace("\n", "")

                # validate row length
                if len(row) != 9:
                    raise ValueError("Row length is not 9")

                # Convert each character to an integer
                try:
                    board.append([int(char) for char in row])
                except ValueError:
                    # if the character is not an integer
                    raise ValueError("Invalid character found")

        # validate board size
        if len(board) != 9:
            raise ValueError("Board size is not 9 x 9")

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
        print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return

    # input file containing sudoku
    input_file = sys.argv[1]

    # initial unsolved sudoku
    sododku_solver = SudokuSolver(input_file)
    print("\nInitial unsolved sudoku: \n\n", np.matrix(sododku_solver.get_board()))

    # final solved sudoku
    sododku_solver.solve_sudoku()
    print("\nFinal solved sudoku: \n\n", np.matrix(sododku_solver.get_board()))
    return


if __name__ == "__main__":
    main()
