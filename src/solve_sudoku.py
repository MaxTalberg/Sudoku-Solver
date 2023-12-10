import sys
import argparse
from sudoku_reader import SudokuReader
from sudoku_board import SudokuBoard
from sudoku_algorithm import SudokuAlgorithm
from sudoku_format import SudokuFormat
from app import app


def main():
    """
    Main function to run the sudoku solver and webapp
    """
    parser = argparse.ArgumentParser(description="Sudoku Solver and Web App")
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Path to the Sudoku puzzle file",
        default=None,
    )
    parser.add_argument(
        "--web", action="store_true", help="Run the web application"
    )

    args = parser.parse_args()

    if args.web:
        # Run the web app
        app.run(host="0.0.0.0", port=80)
    elif args.input_file:
        # Run the Sudoku solver
        reader = SudokuReader(args.input_file)
        sudoku = SudokuBoard(reader.board)
        solver = SudokuAlgorithm(sudoku.board)

        if solver.solve_sudoku():
            formatter = SudokuFormat(solver.board)
            print(formatter.format_sudoku_board())
        else:
            raise ValueError("Unsolvable sudoku")
    else:
        print("Usage: python src/solve_sudoku.py input.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
