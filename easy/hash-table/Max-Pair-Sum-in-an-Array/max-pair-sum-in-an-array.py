#
# @lc app=leetcode id=2815 lang=python
#
# Max Pair Sum in an Array
#

# @lc code=start
class Solution(object):
    def maxSum(self, nums):
        numbers = set() 
        for digit in nums:
            for num in str(digit):
                if int(num) not in numbers:
                    numbers.add(int(num))

        
        seen = {}
        for i in numbers:
            temp = []
            for j in range(len(nums)):
                maximum_temp = []
                for k in range(len(str(nums[j]))):
                    maximum_temp.append(int(str(nums[j])[k]))

                if max(maximum_temp) > i:
                    continue
                elif max(maximum_temp) == i:
                    temp.append(nums[j])
                    
            seen[i] = seen.get(i, temp)
    
    
        res = -1
        for key in seen:
            if len(seen[key]) > 1:
                res = max(res, sum(sorted(seen[key])[-2:]))
        return res

# You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

# Return the maximum sum or -1 if no such pair exists.

 

# Example 1:

# Input: nums = [112,131,411]

# Output: -1

# Explanation:

# Each numbers largest digit in order is [2,3,4].

# Example 2:

# Input: nums = [2536,1613,3366,162]

# Output: 5902

# Explanation:

# All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

# Example 3:

# Input: nums = [51,71,17,24,42]

# Output: 88

# Explanation:

# Each number's largest digit in order is [5,7,7,4,4].

# So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

 

# Constraints:

# 2 <= nums.length <= 100
# 1 <= nums[i] <= 104
        
# @lc code=end

