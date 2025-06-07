#
# @lc app=leetcode id=1189 lang=python
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution(object):
    def maxNumberOfBalloons(self, text):
        baloon = "balloon"
        baloon_seen = {}
        for i in baloon:
            baloon_seen[i] = baloon_seen.get(i, 0) + 1

        text_seen = {}
        for ch in text:
            if ch in baloon:
                text_seen[ch] = text_seen.get(ch, 0) + 1

        minimum = float("inf")
        for key in baloon_seen:
            if key not in text_seen:
                return 0
            minimum = min(minimum, text_seen[key] // baloon_seen[key])

        return minimum
            



        
# @lc code=end

