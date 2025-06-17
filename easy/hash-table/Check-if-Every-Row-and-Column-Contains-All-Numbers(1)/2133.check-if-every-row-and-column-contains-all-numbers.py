#
# @lc app=leetcode id=2133 lang=python3
#
#  Check if Every Row and Column Contains All Numbers
#

# @lc code=start
from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid = set(range(1, n + 1))
        for i in range(n):
            row = set(matrix[i])
            col = set(list(zip(*matrix))[i])

            if row != valid or col != valid:
                return False

        return True

# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

# Example 1:

# Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
# Output: true
# Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
# Hence, we return true.
# Example 2:


# Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
# Output: false
# Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
# Hence, we return false.
 
# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n
# @lc code=end

