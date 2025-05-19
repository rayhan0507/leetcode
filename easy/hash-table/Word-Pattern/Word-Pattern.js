/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
// hash-table O(n)
var wordPattern = function(pattern, s) {
    let s_split = s.split(" ")
    if ((pattern.length == s_split.length) && ([...new Set(pattern)].length == [...new Set(s_split)].length)) {
        let pattern_freq = {}
        for (let i = 0; i < pattern.length; i++) {
            pattern_freq[pattern[i]] = (pattern_freq[pattern[i]] || s_split[i])
        } 

        for (let j = 0; j < pattern.length; j++) {
            if (pattern_freq[pattern[j]] != s_split[j]) {
                return false
            }
        }
        return true
    }
    return false
};
console.log(wordPattern("abba", "dog cat cat dog"))


// Given a pattern and a string s, find if s follows the same pattern.

// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

// Each letter in pattern maps to exactly one unique word in s.
// Each unique word in s maps to exactly one letter in pattern.
// No two letters map to the same word, and no two words map to the same letter.
 

// Example 1:

// Input: pattern = "abba", s = "dog cat cat dog"

// Output: true

// Explanation:

// The bijection can be established as:

// 'a' maps to "dog".
// 'b' maps to "cat".
// Example 2:

// Input: pattern = "abba", s = "dog cat cat fish"

// Output: false

// Example 3:

// Input: pattern = "aaaa", s = "dog cat cat dog"

// Output: false