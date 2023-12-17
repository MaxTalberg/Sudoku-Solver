class SudokuReader:
    """
    Handles the reading of a sudoku board from a
    text file and initialising a sudoku board as
    a list of lists for further processing
    """

    # initialise board from file
    def __init__(self, filename):
        """
        Initialises the SudokuReader class with
        a sudoku board from the given file.

        Parameters
        ----------
        filename : str
            Path to the text file containing the sudoku puzzle.

        Raises
        ------
        RuntimeError
            If the file is not found, invalid or is empty.
        """
        try:
            self.board = self.read_board_from_file(filename)
        except (FileNotFoundError, ValueError) as error:
            raise RuntimeError(f"Failed to initialise board: {error}")

    def read_board_from_file(self, filename):
        """
        Reads a sudoku puzzle from a text file and converts it
        into a list of lists where each sublist represents a row of the sudoku.

        Parameters
        ----------
        filename : str
            Path to the text file containing the sudoku puzzle.

        Returns
        -------
        list[list[str]]
            A 2D list representing each row of the initial sudoku board.

        Raises
        ------
        ValueError
            If the file is not found, invalid or is empty.

        """

        # Initialise the empty board
        board = []

        with open(filename, "r") as file:
            for line_number, line in enumerate(file, 1):
                # Ignore the grid separators
                if line.startswith("---"):
                    continue

                # Remove the grid dividers and newline characters
                row = line.replace("|", "").replace("\n", "")

                # Create list of characters in row
                row_values = [str(char) for char in row]

                # append row to board
                board.append(row_values)

        # Check if file is empty
        if not board:
            raise ValueError("File is empty")

        # Return the matrix of the inserted sudoku board
        return board
