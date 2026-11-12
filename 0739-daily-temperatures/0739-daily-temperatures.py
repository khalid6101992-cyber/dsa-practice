class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:          # blank 1: today is warmer than the day on top
                waiting_day = stack.pop()
                ans[waiting_day] = i - waiting_day    # blank 2: how long it waited
            stack.append(i)                           # blank 3: today starts waiting
        return ans