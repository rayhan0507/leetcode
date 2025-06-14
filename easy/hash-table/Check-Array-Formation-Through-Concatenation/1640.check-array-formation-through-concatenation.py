#
# @lc app=leetcode id=1640 lang=python3
#
#  Check Array Formation Through Concatenation
#

# @lc code=start
from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {p[0]: p for p in pieces} 

        i = 0 
        while i < len(arr):
            if arr[i] not in mapping:
                return False

            part = mapping[arr[i]]
            for num in part:
                if i >= len(arr) or arr[i] != num:
                    return False
                i += 1

        return True
# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

# Example 1:

# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# Explanation: Concatenate [15] then [88]
# Example 2:

# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# Explanation: Even though the numbers match, we cannot reorder pieces[0].
# Example 3:

# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# Explanation: Concatenate [91] then [4,64] then [78]# @lc code=end

