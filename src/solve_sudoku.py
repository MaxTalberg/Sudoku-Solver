import sys
from sudoku_reader import SudokuReader
from sudoku_board import SudokuBoard
from sudoku_algorithm import SudokuAlgorithm
from sudoku_format import SudokuFormat


def main():
    """
    Main function to run the sudoku solver
    """
    # Check the correct number of command line arguements are passsed
    if len(sys.argv) != 2:
        # print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return

    # input file containing sudoku
    input_file = sys.argv[1]

    # read board from file
    reader = SudokuReader(input_file)
    board = reader.board

    # initialise sudoku board
    sudoku = SudokuBoard(board)

    # initialise sudoku algorithm
    solver = SudokuAlgorithm(sudoku.board)

    # solve sudoku
    if solver.solve_sudoku():
        # get formated sudoku board
        formatter = SudokuFormat(solver.board)
        print(formatter.format_sudoku_board())
    else:
        raise ValueError("Unsolvable sudoku")


if __name__ == "__main__":
    main()
