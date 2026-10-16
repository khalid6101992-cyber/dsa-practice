class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedData = sorted(nums)
        result = []
        for i, data in enumerate(sortedData):
            if i > 0 and data == sortedData[i - 1]:
                continue
            target = -(data)
            left = i+1
            right = len(nums) - 1
            while left < right:
                addition = sortedData[left] + sortedData[right]
                if addition < target:
                    left += 1
                elif addition > target:
                    right -= 1
                    
                else:
                    result.append([data, sortedData[left], sortedData[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedData[left] == sortedData[left-1]:
                        left += 1
        return result