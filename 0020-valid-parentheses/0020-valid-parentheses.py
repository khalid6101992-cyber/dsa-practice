class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        ans = []
        for i in s:
            if i in brackets:
                if not ans or ans[-1] != brackets[i]:
                    return False
                ans.pop()
            else:
                ans.append(i)
        if len(ans) == 0:
            return True
        else:
            return False