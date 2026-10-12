# 49. Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/
#
# Approach: sorted letters form a "signature" shared by all anagrams.
#           Use the signature as a dictionary key and collect words in lists.
# Time: O(n * k log k)   Space: O(n * k)
#   n = number of words, k = length of the longest word
#
# Follow-up: use a 26-letter count tuple as the key instead of sorting -> O(n * k).
# Lesson learned: lists can't be dictionary keys, so join sorted letters into a string.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for single_string in strs:
            signature = "".join(sorted(single_string))
            if signature not in groups:
                groups[signature] = []
            groups[signature].append(single_string)
        return list(groups.values())
