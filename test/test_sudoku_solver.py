"""
PROTOTYPING
Read the Sudoku puzzle from input or define it as a 2D array.
Unit testing
- Test with non-existent file
- Test with badly formatted file
- Test with correct file


Implement a function to check if a number is valid:
Unit testing
- Test with true values
- Test with false values columnn and row and 3x3 square
- Test edge cases

Implement a recursive function to solve the Sudoku puzzle using backtracking
based on the validity of the function above.


Potentially another test file for a different more complex algorithm
"""
print("#####\n#####\n####")

from src.sudoku_solver import SudokuSolver
import sys
import numpy as np

# input file containing sudoku
input_file = sys.argv[1]

# Check working
sododku_solver = SudokuSolver(input_file)
print("\nInitial unsolved sudoku: \n\n", np.matrix(sododku_solver.get_board()))