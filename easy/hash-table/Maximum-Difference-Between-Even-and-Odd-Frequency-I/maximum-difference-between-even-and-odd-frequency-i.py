#
# @lc app=leetcode id=3442 lang=python3
#
#  Maximum-Difference-Between-Even-and-Odd-Frequency-I
#

# @lc code=start
class Solution:
    def maxDifference(self, s: str) -> int:
        seen = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1

        even = []
        odd = []
        t = float("-inf")
        for k in seen:
            if seen[k] % 2 == 0:
                even.append(seen[k])
            else:
                odd.append(seen[k])

        for i in odd:
            for j in even:
                t = max(t, i - j)
        
        return t
# @lc code=end

