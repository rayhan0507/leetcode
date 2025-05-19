# https://leetcode.com/problems/word-pattern/

# hash-table O(n)
class Solution(object):
    def wordPattern(self, pattern, s):
        if len(set(pattern)) == len(set(s.split(" "))) and len(pattern) == len(s.split(" ")):
            pattern_freq = {}
            for a, b in zip(pattern, s.split(" ")):
                pattern_freq[a] = pattern_freq.get(a, b)

            for a, b in zip(pattern, s.split(" ")):
                if pattern_freq[a] != b:
                    return False
            return True
        return False

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"

# Output: false

# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"

# Output: false