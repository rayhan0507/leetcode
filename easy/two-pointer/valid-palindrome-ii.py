"""
Deskripsi Soal:
Diberikan sebuah string `s`, tentukan apakah string tersebut bisa menjadi palindrom dengan menghapus paling banyak satu karakter.

Edge Cases:
1.  String kosong: String kosong dianggap sebagai palindrom.
2.  String yang sudah menjadi palindrom: Jika string sudah menjadi palindrom, maka tidak perlu menghapus karakter apa pun.
3.  String yang memerlukan satu penghapusan: String yang bisa menjadi palindrom dengan menghapus satu karakter.
4.  String yang memerlukan lebih dari satu penghapusan: String yang tidak bisa menjadi palindrom dengan menghapus hanya satu karakter.
5.  String dengan semua karakter yang sama: String seperti "aaaaa" sudah menjadi palindrom.
6. String dengan panjang 1: String dengan satu karakter sudah menjadi palindrom.
"""
#
# @lc app=leetcode id=680 lang=python3
#
# Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        def is_palindrome(text):
            l, r = 0, len(text) - 1
            while l < r:
                if text[l] != text[r]:
                    return False
                
                l += 1
                r -= 1

            return True
            
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return is_palindrome(s[i:j]) or is_palindrome(s[i+1:j+1])
            
            i += 1
            j -= 1

        return True



print(Solution().validPalindrome("abc"))
print(Solution().validPalindrome("abca"))
print(Solution().validPalindrome("abcdecba"))
# @lc code=end