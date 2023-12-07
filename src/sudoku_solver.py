import sys
import warnings


class SudokuSolver:
    """Class to solve a sudoku"""

    # initialise board from file
    def __init__(self, filename):
        """
        Initialises the sudoku board from a given file
        """
        try:
            self.board = self.read_board_from_file(filename)
            self.convert_board_to_int()
            for row in self.board:
                print(row)
            self.validate_board()
            print("Post vboard:")
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

                row_values = [str(char) for char in row]

                # append row to board
                board.append(row_values)

        # Return the matrix of the inserted sudoku board
        return board

    def convert_board_to_int(self):
        """
        Converts the board to int

        Returns
        ----------
        board: list(list(int))
            The current state of the sudoku board
        """
        if self.board is None:
            return False
        # initialise empty board
        converted_board = []

        # iterate through each row with row_id
        for row_id, row in enumerate(self.board):
            # initialise empty row
            converted_row = []

            # iterate through each value in row with col_id
            for col_id, value in enumerate(row):
                # convert value to int

                try:
                    # convert value to int
                    int_value = int(value)
                except ValueError:
                    # if value is not int raise error
                    raise ValueError(
                        "Invalid character found at"
                        f"({row_id}, {col_id}): {value}"
                    )

                converted_row.append(int_value)
            converted_board.append(converted_row)
        self.board = converted_board

        # return True if board is valid
        return True

    def validate_board(self):
        """
        Validates the sudoku board

        Parameters
        ----------
        board: list(list(int))
            The current state of the sudoku board

        Returns
        ----------
        board: list(list(int))
            The validated state of the sudoku board
        """
        if self.board is None:
            return False

        # validate board size
        if len(self.board) != 9 or any(len(row) != 9 for row in self.board):
            raise ValueError("Board size is not 9 x 9")

        # Dictionaries to check for duplicates in rows, columns and 3x3 squares
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        # iterate through each row with row_id
        for row_id, row in enumerate(self.board):
            # iterate through each value in row with col_id
            for col_id, value in enumerate(row):
                print(value)
                print(type(value))
                # skip if value is 0 as it is a blank square
                if value == 0:
                    print("continue?")
                    continue

                # validate numbers are between 0 and 9
                if value < 0 or value > 9:
                    raise ValueError("Invalid number found in row")

                # stores and checks for duplicates in rows
                if value in rows[row_id]:
                    print(value, rows[row_id])
                    raise ValueError(
                        f"Duplicate number found in row: {row_id}"
                    )
                rows[row_id].add(value)

                # stores and checks for duplicates in the current column
                if value in cols[col_id]:
                    raise ValueError(
                        f"Duplicate number found in column: {col_id}"
                    )
                cols[col_id].add(value)

                # stores and checks for duplicates in 3x3 square
                square_id = (row_id // 3) * 3 + col_id // 3
                if value in squares[square_id]:
                    raise ValueError(
                        f"Duplicate number found in 3x3 square: {square_id}"
                    )
                squares[square_id].add(value)

        # check row and col length
        for row in self.board:
            if len(row) != 9:
                raise ValueError(
                    f"Row length error row {row} has {len(row)} columns"
                )

        for col_id in range(9):
            if len([self.board[row_id][col_id] for row_id in range(9)]) != 9:
                col_len = len(
                    [self.board[row_id][col_id] for row_id in range(9)]
                )
                raise ValueError(
                    f"Column length error column {col_id} has {col_len} rows"
                )

        # warning if board has less than 17 starting values
        non_zero_count = sum(len(row_len) for row_len in rows)
        if non_zero_count < 17:
            warnings.warn(
                "Warning: Board has less than 17 starting values. "
                "May have multiple solutions."
            )

        # return True if board is valid
        return True

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
            raise ValueError("No board found")
        # checks if square is blank, contains a 0
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    for n in range(1, 10):
                        if self.check_possible_indicies(x, y, n):
                            self.board[y][x] = n
                            if self.solve_sudoku():
                                return True
                            self.board[y][x] = 0
                    # check if square is unsovleable
                    return False

        # If entire board is filled without issues, return True
        return True

    def format_sudoku_board(self):
        """
        Formats the sudoku board

        Returns
        ----------
        formated_board: str
            The formatted sudoku board
        """
        # initialise empty string
        formated_board = ""
        # iterate through each row
        for i, row in enumerate(self.board):
            if i % 3 == 0 and i != 0:
                formated_board += "---+---+---\n"
            # iterate through each number in row
            for j, number in enumerate(row):
                if j % 3 == 0 and j != 0:
                    formated_board += "|"
                formated_board += str(number)
            formated_board += "\n"
        # return formatted board
        return formated_board


def main():
    # Check the correct number of command line arguements are passsed
    if len(sys.argv) != 2:
        # print("Usage: python3 src/sudoku_solver.py data/input.txt")
        return

    # input file containing sudoku
    input_file = sys.argv[1]

    # error handling for unsolvable sudoku
    try:
        # initial unsolved sudoku
        sudoku_solver = SudokuSolver(input_file)
        if sudoku_solver.solve_sudoku():
            # get formated sudoku board
            solved_board = sudoku_solver.format_sudoku_board()
            return print(solved_board)
        else:
            raise ValueError("Unsolvable sudoku")

    except ValueError as e:
        return print(e)


if __name__ == "__main__":
    main()
