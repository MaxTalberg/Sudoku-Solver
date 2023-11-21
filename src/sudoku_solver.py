'''
PROTOTYPING
Read the Sudoku puzzle from input or define it as a 2D array.
Check suduko is valid. 
    - Repeats in row, column or grid.
    - Valid data types numbers 1-9


Implement a function to check if a number is valid:
- in a given row.
- in a given column.
- in a given 3x3 subgrid.

Implement a recursive function to solve the Sudoku puzzle using backtracking
based on the validity of the function above.

Print the solved Sudoku puzzle.
'''
import sys
import numpy as np


def read_board_from_file(filename):
    '''
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

    Add error trapping ---> unit tests
    '''
    # Initialise the empty board
    board = []

    with open(filename, 'r') as file:
        for line in file:

            # Ignore the grid separators
            if line.startswith("---"):
                continue

            # Remove the grid dividers and newline characters, then split into numbers
            row = line.replace('|', '').replace('\n', '')

            # Convert each character to an integer
            board.append([int(char) for char in row])

    # Return the matrix of the inserted sudoku board
    return board

def check_possible_indicies(x, y, n):

    '''
    Checks if a certain indicies is possible
    on a certain grid of the sudoku board

    Parameters
    ----------
    x: int
        grid square number on the x-axis

    y: int
        grid square number on the y-axis

    n: int
        indicie to go into grid square

    Returns
    ----------
    Boolean
        Boolean output to determin if
        intiger is possible

    '''
    # Initialise global variable board
    board = [[0, 0, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 0, 9, 5, 0, 4], [0, 0, 0, 0, 5, 0, 1, 6, 9], [0, 8, 0, 0, 0, 0, 3, 0, 5], [0, 7, 5, 0, 0, 0, 2, 9, 0], [4, 0, 6, 0, 0, 0, 0, 8, 0], [7, 6, 2, 0, 8, 0, 0, 0, 0], [1, 0, 3, 9, 0, 0, 0, 0, 0], [0, 0, 0, 6, 0, 0, 0, 0, 0]]

    # checks if n is in column x
    for i in range(0,9):
        if board[i][x] == n:
            #print('x: ', [x+1, i+1])
            return False
        
    # checks if n is in row y
    for i in range(0,9):
        if board[y][i] == n:
            #print('y: ' ,[i+1, y+1])
            return False
        
    # check if n is in 3x3 square
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == n:
                return False
    # return True if intiger is allowed on square x, y
    return True


def main():

    # Check the correct number of command line arguements are passsed
    if len(sys.argv) != 2:
        print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return

    input_file = sys.argv[1]

    board = read_board_from_file(input_file)

    # readable grid output
    print(np.matrix(board))

    # test to confirm desired output from algorithm
    assert(check_possible_indicies(5, 0, 4) == True)

    return


if __name__ == "__main__":
    main()
    