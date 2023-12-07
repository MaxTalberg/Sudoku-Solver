class SudokuAlgorithm:
    """
    Class to solve the sudoku puzzle
    using the backtracking algorithm
    """

    def __init__(self, board):
        """
        Initialises the sudoku board from
        sudoku_board.py
        """
        self.board = board

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
