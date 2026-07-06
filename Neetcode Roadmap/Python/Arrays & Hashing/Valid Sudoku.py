import collections

"""
Make a program to check whether or not a sudoku board is valid based on the following rules:
    1) Each row must contain the digits 1-9 without duplicates.
    2) Each column must contain the digits 1-9 without duplicates.
    3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

A sudoku needs neither be solvable or full to be valid.


Example 1:
    Input: board =
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","8",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]

    Output: true

Example 2:
    Input: board =
    [["1","2",".",".","3",".",".",".","."],
     ["4",".",".","5",".",".",".",".","."],
     [".","9","1",".",".",".",".",".","3"],
     ["5",".",".",".","6",".",".",".","4"],
     [".",".",".","8",".","3",".",".","5"],
     ["7",".",".",".","2",".",".",".","6"],
     [".",".",".",".",".",".","2",".","."],
     [".",".",".","4","1","9",".",".","8"],
     [".",".",".",".","8",".",".","7","9"]]

    Output: false

https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
"""


def isValidSudoku(board: list[list[str]]) -> bool:
    cols = collections.defaultdict(set)  # empty set for rows
    rows = collections.defaultdict(set)  # empty set for columns
    squares = collections.defaultdict(set)  # empty set for squares
    # each square will be its own

    # sets are unordered data structures that are arranged similar to lists ({1, 2, 3, 4}) except they do not allow duplicate values
    # when using the defaultdict(set) from the collections library, they are arranged more like a hashmap with each value being a set
    #
    # in this case, each row and column index is the key with the sudoku board elements being the values in those columns and rows
    # for example: col: { 0: {"5", "1"}, 1: {"1"}, 2: {}}
    #
    # the squares set treats each square as its own index, this is where the integer division comes into play
    # the the first 3 rows will be at index 0, the next 3 at index 1, and the final 3 at index 2
    # rows 0-2 -> 0, rows 3-5 -> 1, rows 6-8 -> 2
    #
    # the same goes for columns
    #
    # therefore it can be laid out like this:
    #           Col 0-2:      Col 3-5:       Col 6-8:
    # Rows 0-2: Square(0,0)   Square(0,1)    Square(0,2)
    # Rows 3-5: Square(1,0)   Square(1,1)    Square(1,2)
    # Rows 6-8: Square(2,0)   Square(2,1)    Square(2,2)
    #
    # each set of 3 rows x 3 columns is a square, that is why we are able to do it like this. columns 0-2 and rows 0-2 make up 1 square.

    for r in range(9):
        for c in range(9):
            # these loops act like a scanner
            # r -> row index, c -> column index (r, c) pinpoint every single point on the 9x9 grid
            if board[r][c] == ".":  # skip empty cells
                continue
            if (
                board[r][c]
                in rows[
                    r
                ]  # if the current element exists in the current -> invalid board
                or board[r][c]
                in cols[
                    c
                ]  # if the current element exists in the current column -> invalid board
                or board[r][c] in squares[(r // 3, c // 3)]
            ):  # if the current element exists in the current 3x3 square -> invalid board
                return False

            cols[c].add(board[r][c])  # otherwise add the element to the columns set
            rows[r].add(board[r][c])  # otherwise add the element to the rows set
            squares[(r // 3, c // 3)].add(
                board[r][c]
            )  # otherwise add the element to the squares set

    return True


print(
    isValidSudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    isValidSudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
