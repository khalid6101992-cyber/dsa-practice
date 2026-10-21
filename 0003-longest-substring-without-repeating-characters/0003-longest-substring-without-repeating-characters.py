class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lemgthOfLongestString = 0
        left = 0 
        dataset = set()
        for i in s:
            while i in dataset:
                dataset.remove(s[left])
                left += 1
            dataset.add(i)
            lemgthOfLongestString = max(lemgthOfLongestString, len(dataset))
        return lemgthOfLongestString
            