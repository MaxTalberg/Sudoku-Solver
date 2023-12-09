from flask import Flask, request, render_template
from ..sudoku_reader import SudokuReader
from ..sudoku_board import SudokuBoard
from ..sudoku_algorithm import SudokuAlgorithm


# initialise the app
app = Flask(__name__)


# decorator for the home page of the app and defines the upload method
@app.route("/", methods=["GET", "POST"])
def upload():
    error_message = None

    # if the request method is POST the user has uploaded a file
    if request.method == "POST":
        file = request.files.get("file")
        # file saved as input.txt
        if file and file.filename != "":
            filename = "input.txt"
            file.save(filename)

            try:
                # initialise and read the sudoku board
                reader = SudokuReader(filename)
                sudoku = SudokuBoard(reader.board)
                board = sudoku.board
                # render the sudoku board
                return render_template(
                    "sudoku_board.html",
                    board=board,
                    error_message=error_message,
                )
            except ValueError as e:
                # displays error messages from
                # src/sudoku_reader.py and src/sudoku_board.py
                error_message = str(e)

        else:
            error_message = "No file selected"
    # if the request method is GET the user has not uploaded a file
    return render_template(
        "sudoku_board.html", board=None, error_message=error_message
    )


# decorator for the solve method
@app.route("/solve", methods=["POST"])
def solve():
    error_message = None

    try:
        # solve sudoku board labelled as input.txt
        filename = "input.txt"
        reader = SudokuReader(filename)
        sudoku = SudokuBoard(reader.board)
        board = sudoku.board
        solver = SudokuAlgorithm(board)
        solver.solve_sudoku()
        if solver.solve_sudoku():
            board = solver.board
            # render the solved sudoku board
            return render_template(
                "sudoku_board.html", board=board, error_message=error_message
            )
        else:
            error_message = "Unsolvable sudoku"
    except ValueError as e:
        # displays error messages from src/sudoku_algorithm.py
        error_message = str(e)

    return render_template(
        "sudoku_board.html", board=None, error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
