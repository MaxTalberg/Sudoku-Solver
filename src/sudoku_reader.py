class SudokuReader:
    """
    Class to read sudoku board
    from a text file
    """

    # initialise board from file
    def __init__(self, filename):
        """
        Initialises the sudoku board from a given file
        """
        try:
            self.board = self.read_board_from_file(filename)
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
