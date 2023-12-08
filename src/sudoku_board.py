import warnings


class SudokuBoard:
    """
    Handles the validation process of the sudoku board
    from a 2D list and converts the board to integers
    """

    def __init__(self, board):
        """
        Initialises the SudokuBoard class by converting
        the input string into integers and validating the
        rules of sudoku are met and edge cases are covered

        Parameters
        ----------
        board : list[list[str]]
            The current state of the sudoku board as a list of string lists.

        Raises
        ------
        ValueError
            If the conversion to integers fails or the board is not valid.

        """
        self.board = board

        if not self.convert_board_to_int():
            raise ValueError("Failed to convert board to integers")

        if not self.validate_board():
            raise ValueError("Failed to validate board")

    def convert_board_to_int(self):
        """
        Converts the 2D list of strings to a
        2D list of integers

        Returns
        -------
        bool:
            True if the sudoku board is valid

        Raises
        ------
        ValueError:
            If the board is not initialised or contains invalid characters
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
        Validates the sudoku board by:
            - Ensuring the board is initialised
            - Checks the board size is 9x9
            - Checks for invalid numbers outside of 0-9
            - Detects duplicates in rows, columns and 3x3 squares
            - Confirms each row and column is of 9

        Issues warnings:
            - For boards with has less than 17 starting values
            - For empty boards

        Returns
        -------
        bool:
            True is the board is valid, False otherwise

        Raises
        ------
        ValueError:
            If the board is not initialised
            If the board size is not 9x9
            If the board contains invalid numbers outside of 0-9
            If the board contains duplicates in rows, columns or 3x3 squares
            If the row or column length is not 9

        Warnings
        --------
        UserWarning:
            If the board has less than 17 starting values or is empty

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
