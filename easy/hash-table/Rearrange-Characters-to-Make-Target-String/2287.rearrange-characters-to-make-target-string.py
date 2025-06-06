#
# @lc app=leetcode id=2287 lang=python
#
# [2287] Rearrange Characters to Make Target String
#

# @lc code=start
class Solution(object):
    def rearrangeCharacters(self, s, target):
        t_seen = {}
        for i in target:
            t_seen[i] = t_seen.get(i, 0) + 1

        s_seen = {}
        for i in s:
            if i in target:
                s_seen[i] = s_seen.get(i, 0) + 1

        minimum = float("inf")
        for key in t_seen:
            if key not in s_seen:
                return 0
            minimum = min(minimum, s_seen[key] // t_seen[key])

        return minimum 
        
# @lc code=end

