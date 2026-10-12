# 128. Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Approach: put numbers in a set. A number is the BEGINNING of a run if
#           (num - 1) is missing. From each beginning, count upward.
# Time: O(n) - each number is visited by at most one counting walk
# Space: O(n)
#
# Lessons learned:
#   - loop over the set, not the list, so duplicates don't repeat work (TLE)
#   - use max() so a shorter later run doesn't overwrite a longer one
#   - return only after the loop ends

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        groups = set(nums)
        longest = 0
        for num in groups:
            if num - 1 not in groups:
                length = 1
                while num + length in groups:
                    length += 1
                longest = max(longest, length)
        return longest
