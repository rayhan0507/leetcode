# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=problem-list-v2&envId=hash-table

# hashmap O(n)
class Solution(object):
    def maxFreqSum(self, s):
        vowels = {}
        consonant = {}
        for i in s:
            if i.lower() in "aiueo":
                vowels[i] = vowels.get(i, 0) + 1
            else:
                consonant[i] = consonant.get(i, 0) + 1

        max_vowels = 0
        max_consonant = 0
        for vowels_val in vowels.values():
            max_vowels = max(max_vowels, vowels_val)

        for consonant_val in consonant.values():
            max_consonant = max(max_consonant, consonant_val)

        return max_vowels + max_consonant
    
# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.
 

# Example 1:

# Input: s = "successes"

# Output: 6

# Explanation:

# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.
# Example 2:

# Input: s = "aeiaeia"

# Output: 3

# Explanation:

# The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
# There are no consonants in s. Hence, maximum consonant frequency = 0.
# The output is 3 + 0 = 3.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters only.