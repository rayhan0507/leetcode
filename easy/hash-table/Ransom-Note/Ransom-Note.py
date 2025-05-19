# https://leetcode.com/problems/ransom-note/?envType=problem-list-v2&envId=hash-table

# hash-table O(n)
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq = {}
        for i in ransomNote:
            freq[i] = freq.get(i, 0) + 1

        freq_magazine = {}
        for i in magazine:
            freq_magazine[i] = freq_magazine.get(i, 0) + 1

        for items in freq:
            if freq[items] > freq_magazine.get(items, 0):
                return False
        return True

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.