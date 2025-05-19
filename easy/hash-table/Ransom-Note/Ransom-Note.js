// https://leetcode.com/problems/ransom-note/?envType=problem-list-v2&envId=hash-table

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */

//hash-table O(n)
var canConstruct = function(ransomNote, magazine) {
    let ransomnote_freq = {}
    let magazine_freq = {}
    
    for (let i of ransomNote) {
        ransomnote_freq[i] = (ransomnote_freq[i] || 0) + 1
    }

    for (let i of magazine) {
        magazine_freq[i] = (magazine_freq[i] || 0) + 1
    }

    for (let items in ransomnote_freq) {
        let ransomnote_val = (ransomnote_freq[items] || 0) 
        let magazine_val = (magazine_freq[items] || 0)
        if (ransomnote_val > magazine_val) {
            return false
        }
    }
    return true
};

// Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

 

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false
// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true
 

// Constraints:

// 1 <= ransomNote.length, magazine.length <= 105
// ransomNote and magazine consist of lowercase English letters.