# 125. Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/
#
# Approach 1 - clean first, then two pointers:   Time O(n)   Space O(n)
# Approach 2 - skip non-alphanumerics in place:  Time O(n)   Space O(1)


class SolutionClean:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        start = 0
        end = len(clean) - 1
        while start < end:
            if clean[start] != clean[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
