class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenLongetString = 0
        dataSet = set()
        left = 0
        right = len(s) - 1
        for i in s:
            while i in dataSet:
                dataSet.remove(s[left])
                left += 1
            dataSet.add(i)
            lenLongetString = max(lenLongetString, len(dataSet))
        return lenLongetString