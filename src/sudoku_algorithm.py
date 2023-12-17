class SudokuAlgorithm:
    """
    Handles the solving process of the sudoku board via a backtracking
    algorithm. This class converts an unsovled 2D list to a solved 2D list
    """

    def __init__(self, board):
        """
        Initialises the SudokuAlgorithm with a given sudoku board

        Parameters
        ----------
        board : list[list[int]]
            The current state of the sudoku board.

        """
        self.board = board

    def check_possible_indicies(self, x, y, n):
        """
        Checks if a certain indicies is possible
        on a certain grid of the sudoku board

        Parameters
        ----------
        x : int
            Column number of the sudoku board.
        y : int
            Row number of the sudoku board.
        n : int
            Number to check in the grid square.

        Returns
        -------
        bool:
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

    def find_mrv_cell(self):
        """
        Finds the cells with the minimum remaining values (MRV)
        and returns the cell with the least amount of possible values

        Returns
        -------
        tuple:
            The x and y coordinate of the cell with the least amount of
            possible values or None if no cell exists
        """
        # initial mrv score greater than any possible score
        mrv = 10
        mrv_cell = None

        # iterate through each cell
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == 0:
                    # find number of possible values for cell
                    possible_values = sum(
                        self.check_possible_indicies(x, y, n)
                        for n in range(1, 10)
                    )
                    if possible_values < mrv:
                        mrv = possible_values
                        mrv_cell = (x, y)

        return mrv_cell

    def solve_sudoku(self):
        """
        Solves the sudoku by recurssion of possbile indicies
        this function utlises the backtracking algorithm

        Returns
        -------
        bool:
            True if the board is solved, False otherwise
        """
        if self.board is None:
            raise ValueError("No board found")

        # find the cell with the least amount of possible values
        mrv_cell = self.find_mrv_cell()
        if mrv_cell is None:
            return True

        # unpack the tuple
        x, y = mrv_cell

        # recurse through each possible value
        for n in range(1, 10):
            if self.check_possible_indicies(x, y, n):
                self.board[y][x] = n
                if self.solve_sudoku():
                    return True
                self.board[y][x] = 0
        # check if board is unsovleable
        return False
