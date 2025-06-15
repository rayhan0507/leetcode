#
# @lc app=leetcode id=953 lang=python3
#
#  Verifying-an-Alien-Dictionary
#

# @lc code=start
from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx: dict[str, int] = {}
        for ch in range(len(order)):
            order_idx[order[ch]] = ch

        for i in range(len(words) - 1):
            f = words[i]
            l = words[i + 1]
            
            j = 0
            while j < min(len(f), len(l)):
                w_1 = order_idx[f[j]] 
                w_2 = order_idx[l[j]] 
                if w_1 < w_2:
                    break
                elif w_1 > w_2:
                    return False    
                j += 1


            if len(f) > len(l) and f[:len(l)] == l:
                return False

        return True

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
# @lc code=end

