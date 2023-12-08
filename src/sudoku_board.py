import warnings


class SudokuBoard:
    """
    Class to deal with the sudoku board
    """

    def __init__(self, board):
        """
        Initialises the sudoku board from
        sudoku_reader.py
        """
        self.board = board

        if not self.convert_board_to_int():
            raise ValueError("Failed to convert board to integers")

        if not self.validate_board():
            raise ValueError("Failed to validate board")

    def convert_board_to_int(self):
        """
        Converts the board to int

        Returns
        ----------
        board: list(list(int))
            The current state of the sudoku board
        """
        if self.board is None:
            raise ValueError("Board is not initialised")

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
        # check for empty board
        if self.board is None:
            raise ValueError("Board is not initialised")

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
                # skip if value is 0 as it is a blank square
                if value == 0:
                    continue

                # validate numbers are between 0 and 9
                if value < 0 or value > 9:
                    raise ValueError("Invalid number found in row")

                # stores and checks for duplicates in rows
                if value in rows[row_id]:
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
        if non_zero_count == 0:
            warnings.warn("Warning: Board is empty")

        # return True if board is valid
        return True
