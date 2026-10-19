class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lengthOfLongestStr = 0
        dataSet = set()
        left = 0
        for right in range(len(s)):
            while s[right] in dataSet:
                dataSet.remove(s[left])        # blank 1: which letter leaves?
                left += 1
            dataSet.add(s[right])               # blank 2: which letter joins?
            lengthOfLongestStr = max(lengthOfLongestStr, len(dataSet))   # blank 3: window length
        return lengthOfLongestStr