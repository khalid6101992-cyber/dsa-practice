# 347. Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Approach 1 - sort by count:          Time O(n log n)   Space O(n)
# Approach 2 - bucket sort ("shelves"): Time O(n)        Space O(n)
#   A number appears at most n times, so make n + 1 shelves.
#   The count decides the shelf; the number goes on the shelf.
#   Walk from the top shelf down, picking up numbers until we have k.


class SolutionSort:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        ordered = sorted(counts, key=counts.get, reverse=True)
        return ordered[:k]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
