// https://leetcode.com/problems/first-unique-character-in-a-string/description/

// hash-table O(n)
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let freq = {}
    for (const i of s) {
        freq[i] = (freq[i] || 0) + 1
    }

    for (let i = 0; i < s.length; i++) {
        if (freq[s[i]] === 1) {
            return i
        }
    }
    return -1
};


// Input: s = "loveleetcode"

// Output: 2

// Example 3:

// Input: s = "aabb"

// Output: -1

 

// Constraints:

// 1 <= s.length <= 105
// s consists of only lowercase English letters.