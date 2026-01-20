"""
Docstring for valid_sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Time: O(1)
Space: O(1)
Link: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
"""
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        for b_row in range(0,9,3):
            for b_col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[b_row+i][b_col+j]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        return True