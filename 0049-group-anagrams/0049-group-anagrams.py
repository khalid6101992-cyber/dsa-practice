class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        data = {}
        for strings in strs:
            sortedValue = "".join(sorted(strings))
            if sortedValue not in data:
                data[sortedValue] = []
            data[sortedValue].append(strings)
        return list(data.values())

