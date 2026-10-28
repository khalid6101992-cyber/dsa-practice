class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedValues = sorted(nums)
        result = []
        for i, num in enumerate(sortedValues):
            if i > 0 and sortedValues[i] == sortedValues[i - 1]:
                        continue
            fixed = sortedValues[i]
            target = -(fixed)
            left = i+1
            right = len(sortedValues) - 1
            while left < right :

                if target > (sortedValues[left] + sortedValues[right]):
                    left += 1
                elif target < (sortedValues[left] + sortedValues[right]):
                    right -= 1
                else:
                    result.append([sortedValues[i], sortedValues[left], sortedValues[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedValues[left] == sortedValues[left - 1]:
                        left += 1
                    
        return result