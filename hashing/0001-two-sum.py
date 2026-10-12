# 1. Two Sum (Easy)
# https://leetcode.com/problems/two-sum/
#
# Approach: store number -> index in a dictionary. For each number, check
#           whether its partner (target - num) was already stored.
#           Check BEFORE storing, so a number never pairs with itself.
# Time: O(n)   Space: O(n)
#
# Lesson learned: store the current number (num), not the partner (needed).

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans = {}
        for index, num in enumerate(nums):
            needed = target - num
            if needed in ans:
                return [ans[needed], index]
            ans[num] = index
