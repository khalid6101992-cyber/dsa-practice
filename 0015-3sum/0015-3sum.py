class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedNums = sorted(nums)
        result = []
       
        for i,num in enumerate(sortedNums):
            left = i + 1
            right = len(sortedNums) - 1
            if i > 0 and num == sortedNums[i - 1]:
                continue
            while left < right:
                target = -num
                if target > sortedNums[left] + sortedNums[right]:
                    left += 1
                elif  target < sortedNums[left] + sortedNums[right]:
                    right -= 1
                else:
                    result.append([num, sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
        return result
