import unittest
from src.sudoku_format import SudokuFormat


class TestSudokuFormat(unittest.TestCase):
    """
    Test cases for the SudokuFormat class

    The SudokuFormat class is responsible for converting the solved
    sudoku 2D list into the correct format for printing to the console.
    """

    def test_correct_formatting(self):
        """
        Test that the class formats the
        solved sudoku board correctly
        """
        solved_board = [
            [5, 9, 4, 1, 6, 7, 8, 3, 2],
            [6, 1, 8, 2, 3, 9, 5, 7, 4],
            [2, 3, 7, 4, 5, 8, 1, 6, 9],
            [9, 8, 1, 7, 2, 6, 3, 4, 5],
            [3, 7, 5, 8, 4, 1, 2, 9, 6],
            [4, 2, 6, 3, 9, 5, 7, 8, 1],
            [7, 6, 2, 5, 8, 4, 9, 1, 3],
            [1, 4, 3, 9, 7, 2, 6, 5, 8],
            [8, 5, 9, 6, 1, 3, 4, 2, 7],
        ]

        expected_formatted_board = (
            "594|167|832\n"
            "618|239|574\n"
            "237|458|169\n"
            "---+---+---\n"
            "981|726|345\n"
            "375|841|296\n"
            "426|395|781\n"
            "---+---+---\n"
            "762|584|913\n"
            "143|972|658\n"
            "859|613|427\n"
        )

        formatter = SudokuFormat(solved_board)
        self.assertEqual(
            formatter.format_sudoku_board(), expected_formatted_board
        )


if __name__ == "__main__":
    unittest.main()
