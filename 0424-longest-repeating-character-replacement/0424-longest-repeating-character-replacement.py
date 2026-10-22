class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        counts = {}
        left = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            else:
                best = max(best, right - left + 1 )
        return best
