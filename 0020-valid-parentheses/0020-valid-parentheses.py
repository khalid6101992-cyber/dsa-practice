class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')':'(','}':'{',']':'['}

        for i,ch in enumerate(s):
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            
            else:
                stack.append(ch)
        return len(stack) == 0

        