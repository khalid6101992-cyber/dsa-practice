class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        notebook = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in notebook:
                return [notebook.get(needed), i]
            notebook[num] = i

        