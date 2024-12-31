from __future__ import annotations
import numpy as np
"""
  
  [[_, _, _,_, _, _, _, _, _], i = 0
   [_, _, _,_, _, _, _, _, _],  i = 1
   [_, _, _,_, _, _, _, _, _],  i = 2
   [_, _, _,_, _, _, _, _, _],  i = 3
   [_, _, _,_, _, _, _, _, _],  i = 4
   [_, _, _,_, _, _, _, _, _],  i = 5
   [_, _, _,_, _, _, _, _, _],  i = 6
   [_, _, _,_, _, _, _, _, _],  i = 7
   [_, _, _,_, _, _, _, _, _], i = 8
    ]      
""" 
class Sudoku:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.squares = int(self.rows ** 0.5) # square root of 9 is 3, so 3x3 grid. 
    def is_group(self, group: list[int]) -> bool:
        nums = [num for num in group if num != 0] #ignoring empty cells
        
        return len(nums) == len(set(nums)) #if all numbers are unique, then it's a valid group
        
    def is_valid(self, board) -> bool:
        
        # Check rows
        for row in board:
            if not self.is_group(row):
                return False
        #Check  columns
        for col in range(9):
            if not self.is_group([board[row][col] for row in range(9)]):
                return False
        
        #Check 3x3 squares
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                if not self.is_group(square):
                    return False
        return True
    def possibleEntry(self, board: list[list[int]], row: int, col: int, entry: int) -> bool:
        # Check row
        for x in range(0, 9):
            if board[row][x] == entry:
                return False
        #Check Column 
        for y in range(0, 9):
            if board[y][col] == entry:  
                return False
        
        #Check 3x3 square
        squareRowInd = (row//3) * 3
        squareColInd = (col//3) * 3
        for r in range(0, 3):
            for c in range(0, 3):
                if board[squareRowInd + r][squareColInd + c] == entry:
                    return False
        
        return True
    
    #Brute Force Technique
    def solve(self, board: list[list[int]]) -> list[list[int]]:
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == 0:
                    for entry in range(1, self.rows + 1):
                        if self.possibleEntry(board, row, col, entry):
                            board[row][col] = entry
                            if self.solve(board):
                                return board
                            board[row][col] = 0

                    return None
        return board

if __name__ == "__main__":

    #valid board
    valid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

    sudoku1 = Sudoku(valid_board)
    print(np.matrix(valid_board))
    print("This board is valid: ", sudoku1.is_valid(valid_board)) #True

    invalid_board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],  
        [6, 7, 2, 1, 9, 5, 3, 4, 8],  
        [1, 9, 8, 3, 4, 2, 5, 6, 7],  
        [8, 5, 9, 7, 6, 1, 4, 2, 3],  
        [4, 2, 6, 8, 5, 3, 7, 9, 1],  
        [7, 1, 3, 9, 2, 4, 8, 5, 6],  
        [9, 6, 1, 5, 3, 7, 2, 8, 4],  
        [2, 8, 7, 4, 1, 9, 6, 3, 5],  
        [3, 4, 5, 2, 8, 6, 1, 7, 7],
        ]
    sudoku2 = Sudoku(invalid_board)

    print("This board is invalid: ", sudoku2.is_valid(invalid_board)) #False

    valid_incomplete_sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    sudoku3 = Sudoku(valid_incomplete_sudoku_board)
    print("This board is valid: ", sudoku3.is_valid(valid_incomplete_sudoku_board))
    print(sudoku3.possibleEntry(valid_incomplete_sudoku_board, 1, 1, 2))
    complete_board = sudoku3.solve(valid_incomplete_sudoku_board)
    if complete_board:

        print(np.matrix(complete_board))
    else: 
        print(" a solution doesn't exist or was not found. ")


