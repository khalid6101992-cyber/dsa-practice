class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        s2Dict = {}
        for i in s1:
            need[i] = need.get(i, 0) + 1
        for i in range(len(s2)):
            s2Dict[s2[i]] = s2Dict.get(s2[i], 0) + 1

            if i >= len(s1):
                out = s2[i - len(s1)]
                s2Dict[out] -= 1
                if s2Dict[out] == 0:
                    del s2Dict[out]
            if s2Dict == need:
                return True
        return False

        