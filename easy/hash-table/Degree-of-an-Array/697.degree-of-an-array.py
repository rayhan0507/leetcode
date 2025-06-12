#
# @lc app=leetcode id=697 lang=python3
#
#  Degree-of-an-Array
#

# @lc code=start
from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        seen = {}
        first_index = {}
        last_index = {}
        
        for i in range(len(nums)):
            val = nums[i]
            if val not in seen:
                seen[val] = 0
                first_index[val] = i

            seen[val] += 1
            last_index[val] = i


        degree = 0
        for k in seen:
            if seen[k] > degree:
                degree = seen[k]
        
        min_length = len(nums) + 1
     
        for key in seen:
            if seen[key] == degree:
                
                min_length = min(min_length, last_index[key] - first_index[key] + 1)

        return min_length
# @lc code=end
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

