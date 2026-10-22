class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        if len(s1) > len(s2):
            return False
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1
            if right >= len(s1):
                out = s2[right - len(s1)]
                window[out] -= 1
                if window[out] == 0:
                    del window[out]
            if window == need:
                return True
        return False