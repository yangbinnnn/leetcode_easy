# -*- coding:utf-8 -*-
# Author: yangbin
# Created: 04/01/2018

# http://sudoku.com.au/TheRules.aspx

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and \
               self.isValidCol(board) and \
               self.isValidSubBox(board)

    def isValidRow(self, board):
        for row in board:
            if not self.isOnce(row):
                return False
        return True

    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isOnce(col):
                return False
        return True

    def isValidSubBox(self, board):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                nums = [board[m][n] for m in range(i, i+3) for n in range(j, j+3)]
                if not self.isOnce(nums):
                    return False
        return True

    def isOnce(self, nums):
        nums = [num for num in nums if num != '.']
        return len(nums) == len(set(nums))
