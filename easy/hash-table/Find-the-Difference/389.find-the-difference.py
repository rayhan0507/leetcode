#
# @lc app=leetcode id=389 lang=python
#
# [389] Find-the-Difference
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        t_seen = {}
        for ch in t:
            t_seen[ch] = t_seen.get(ch, 0) + 1

        s_seen = {}
        for ch in s:
            s_seen[ch] = s_seen.get(ch, 0) + 1

        for key in t_seen:
            if t_seen.get(key, 0) - s_seen.get(key, 0) != 0:
                return key
        
# @lc code=end

