# https://leetcode.com/problems/count-the-number-of-special-characters-i/

# set O(n)
class Solution(object):
    def numberOfSpecialChars(self, word):
        upper = set([x.lower() for x in word if x.isupper()])
        lower = set([x for x in word if x.islower()])
        return len(list(upper & lower))

# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.

 

# Example 1:

# Input: word = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters in word are 'a', 'b', and 'c'.

# Example 2:

# Input: word = "abc"

# Output: 0

# Explanation:

# No character in word appears in uppercase.

# Example 3:

# Input: word = "abBCab"

# Output: 1

# Explanation:

# The only special character in word is 'b'.