class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        parenthesis = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for ch in s:
            if ch in parenthesis:
                if not result or result[-1] != parenthesis[ch]:
                    return False
                result.pop()
            else:
                result.append(ch)
        return len(result) == 0
