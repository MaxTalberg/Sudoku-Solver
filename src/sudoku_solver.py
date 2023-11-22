'''
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


def check_possible_indicies(board, x, y, n):

    '''
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

    '''

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
        
    # top left corner of 3x3 square
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    # checks if n is in 3x3 square
    for i in range(0,3):
        for j in range(0,3):
            if board[y0 + i][x0 + j] == n:
                return False
            
    # return True if intiger is allowed on square x, y
    return True

def solve_sudoku(board):
    '''
    Solves the sudoku by recurssion of
    possbile indicies

    Parameters
    ----------
    board: list(list(int))
        The current state of the sudoku board

    Returns
    ----------
    Matrix
        Matrix of completed sudoku board!

    '''
    # checks if square is blank, contains a 0
    for x in range(0,9):
        for y in range(0,9):
            if board[y][x] == 0:

                # check if number n can be here
                for n in range(1,10):
                    if check_possible_indicies(board, x,y,n):
                        board[y][x] = n
                        if solve_sudoku(board):
                            return board
                        # backtracking!
                        board[y][x] = 0
                return None
    return board
def main():

    # Check the correct number of command line arguements are passsed
    if len(sys.argv) != 2:
        print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return
    
    # input file containing sudoku
    input_file = sys.argv[1]

    # initial unsolved sudoku
    board = read_board_from_file(input_file)
    print('\nInitial unsolved sudoku: \n\n', np.matrix(board))

    # final solved sudoku
    solved_board = solve_sudoku(board)
    print('\nFinal solved sudoku: \n\n', np.matrix(solved_board))


    return


if __name__ == "__main__":
    main()
    