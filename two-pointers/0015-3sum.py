# 15. 3Sum (Medium)
# https://leetcode.com/problems/3sum/
#
# Approach: sort, then fix one number and run Two Sum II on the numbers to its
#           right, looking for a pair that sums to -(fixed number).
#           Duplicates are removed with a set of tuples: since the list is
#           sorted, every triplet is built in the same order, so repeats match.
# Time: O(n^2)   Space: O(n) plus the set of answers
#
# Next step: skip duplicate fixed numbers and pairs directly (no set needed).

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_data = sorted(nums)
        result = set()

        for index, data in enumerate(sorted_data):
            target = -data
            left = index + 1
            right = len(sorted_data) - 1
            while left < right:
                pair_sum = sorted_data[left] + sorted_data[right]
                if pair_sum < target:
                    left += 1
                elif pair_sum > target:
                    right -= 1
                else:
                    result.add((data, sorted_data[left], sorted_data[right]))
                    left += 1
                    right -= 1
        return [list(t) for t in result]
