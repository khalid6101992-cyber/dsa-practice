# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
#
# Approach: count letters in both strings and compare the counts.
#           Different lengths can never be anagrams, so exit early.
# Time: O(n)   Space: O(1) - at most 26 lowercase letters per dictionary
#
# Lesson learned: Python uses False/True (capitalized), not false/true.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        source = {}
        target = {}
        for ch in s:
            source[ch] = source.get(ch, 0) + 1
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        return source == target
