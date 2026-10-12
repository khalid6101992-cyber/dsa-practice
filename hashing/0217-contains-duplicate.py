# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/
#
# Approach: "Have I seen this before?" -> keep a set of numbers seen so far.
#           Set lookups are O(1), avoiding the O(n^2) nested-loop comparison.
# Time: O(n)   Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
