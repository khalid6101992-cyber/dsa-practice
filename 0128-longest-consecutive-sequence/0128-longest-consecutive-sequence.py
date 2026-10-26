class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        resultData = set(nums)
        longest = 0
        for num in resultData:
            if (num - 1) not in resultData:
                length = 1
                while(num + length in resultData):
                    length += 1
                longest = max(longest, length)
        return longest