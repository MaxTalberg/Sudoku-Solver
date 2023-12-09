from flask import Flask, request, render_template
from sudoku_solver import SudokuSolver
import sys

sys.path.insert(1, "src/")


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload():
    error_message = None

    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename != "":
            filename = "input.txt"
            file.save(filename)

            try:
                # initialise and solve sudoku
                sudoku_solver = SudokuSolver(filename)
                board = sudoku_solver.board
                return render_template(
                    "sudoku_board.html",
                    board=board,
                    error_message=error_message,
                )
            except ValueError as e:
                error_message = str(e)

        else:
            error_message = "No file selected"

    return render_template(
        "sudoku_board.html", board=None, error_message=error_message
    )


@app.route("/solve", methods=["POST"])
def solve():
    error_message = None

    try:
        filename = "input.txt"
        sudoku_solver = SudokuSolver(filename)
        if sudoku_solver.solve_sudoku():
            board = sudoku_solver.get_board()
            return render_template(
                "sudoku_board.html", board=board, error_message=error_message
            )
        else:
            error_message = "Unsolvable sudoku"
    except ValueError as e:
        error_message = str(e)

    return render_template(
        "sudoku_board.html", board=None, error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
