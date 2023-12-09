from flask import Flask, request, render_template
from ..sudoku_reader import SudokuReader
from ..sudoku_board import SudokuBoard
from ..sudoku_algorithm import SudokuAlgorithm


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
                reader = SudokuReader(filename)
                sudoku = SudokuBoard(reader.board)
                board = sudoku.board
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
        reader = SudokuReader(filename)
        sudoku = SudokuBoard(reader.board)
        board = sudoku.board
        solver = SudokuAlgorithm(board)
        solver.solve_sudoku()
        if solver.solve_sudoku():
            board = solver.board
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
