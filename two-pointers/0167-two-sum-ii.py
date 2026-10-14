# 167. Two Sum II - Input Array Is Sorted (Medium)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Approach: the list is sorted, so use two pointers from both ends.
#           Sum too big -> move right left. Too small -> move left right.
#           One loop, one decision per round.
# Time: O(n)   Space: O(1)
#
# Compare with Two Sum (#1): unsorted input needs a dictionary (O(n) space);
# sorted input lets two pointers do it with O(1) space.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
