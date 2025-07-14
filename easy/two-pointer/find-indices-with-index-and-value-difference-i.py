#
# @lc app=leetcode id=2903 lang=python3
#
# [2903] Find Indices With Index and Value Difference I
#
# Deskripsi Soal:
# Diberikan sebuah array integer 0-indexed `nums` dan dua integer, `indexDifference` dan `valueDifference`.
# Tugas Anda adalah menemukan dua indeks `i` dan `j`, keduanya dalam rentang `[0, n - 1]`, yang memenuhi kondisi berikut:
# - `abs(i - j) >= indexDifference`, dan
# - `abs(nums[i] - nums[j]) >= valueDifference`
# Kembalikan `[i, j]` jika indeks tersebut ada. Jika ada beberapa pasang, kembalikan salah satunya.
# Jika tidak ada indeks seperti itu, kembalikan `[-1, -1]`.
#
# Edge Cases:
# - `nums` bisa kosong.
# - `indexDifference` bisa 0.
# - `valueDifference` bisa 0.
# - Tidak ada pasangan indeks yang memenuhi kondisi.
#

# @lc code=start
from typing import List
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if not nums:
            return [-1, -1]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1,-1]
        
# @lc code=end