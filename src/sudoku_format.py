class SudokuFormat:
    """
    Class to deal with the sudoku board
    """

    def __init__(self, board):
        """
        Initialises the sudoku board from
        sudoku_algorithm.py
        """
        self.board = board

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
