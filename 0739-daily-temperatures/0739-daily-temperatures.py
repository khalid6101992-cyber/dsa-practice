class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and (temp > temperatures[stack[-1]]):
                waiting_day = stack.pop()
                ans[waiting_day] = i - waiting_day
            stack.append(i)
        return ans
        